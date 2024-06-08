import os
import keras as k
from keras import models
from keras import layers
import pandas as pd
import numpy as np
import app.domain.helpers.utils as f
import app.domain.helpers.intervals as intervals
from app.domain.columns import names_input


def start(need_train, filename):
    data_frame = pd.read_csv(os.getcwd() + "/output/validated/" + filename + ".csv", delimiter=";")  # подгружаем файл
    data_frame.drop(columns=data_frame.columns[0], axis=1, inplace=True)  # убираем лишний столбец
    data_frame = data_frame.loc[data_frame['anomaly_intensity'] == 1]  # Исключаем строки с выбросами интенсивности
    data_frame.info()
    input_names = names_input()
    if need_train:
        output_names = ["intensity"]  # Интенсивность
    else:
        output_names = []

    encoders = {
        "week_day": lambda value: f.to_binary_equal(value, intervals.day_of_the_week(), False),  # День недели
        "intensity": lambda value: f.to_binary_range(value, intervals.get_intensive_interval(), False),  # Интенсивность
        "day_time": lambda value: f.to_binary_equal(value, intervals.times_of_day(), False),  # Время суток
        't_air': lambda value: f.to_binary_range(value, intervals.get_air_temp_interval(), False),
        # Температура воздуха (t воздуха), С°
        't_soil': lambda value: f.to_binary_range(value, intervals.get_air_temp_interval(), False),
        # Температура почвы (t почвы), С°
        't_dew_point': lambda value: f.to_binary_range(value, intervals.get_air_temp_interval(), False),
        # Температура точки росы (DP), С°
        'partial_pressure': lambda value: f.to_binary_range(value, intervals.get_pressure_interval(), False),
        # Парциальное давление водяного пара (ps), Па
        'humidity': lambda value: f.to_binary_range(value, intervals.get_air_humidity(), False),
        # Относительная влажность воздуха (ϕ), %;
        'saturation_deficit': lambda value: f.to_binary_range(value, intervals.get_saturation_deficit_interval(),
                                                              False),  # Дефицит насыщения (d), г/м³
        'pressure_station': lambda value: f.to_binary_range(value, intervals.get_atmosphere_pressure_station(), False),
        # Атмосферное давление на уровне станции (P станции), г.Па
        'pressure_sea': lambda value: f.to_binary_range(value, intervals.get_atmosphere_pressure_sea(), False),
        # Атмосферное давление на уровне моря (P моря), г.Па
        'visibility_VV': lambda value: f.to_binary_equal(value, intervals.get_visibility(), False),
        # Видимость, шифр (VV);
        'weather_WW': lambda value: f.to_binary_equal(value, intervals.weather_cipher_ww(), False),  # Погода, шифр (ww)
        'wind_direction': lambda value: f.direction_wind_to_matrix(value),  # Направление ветра, градусы
        'wind_speed': lambda value: f.to_binary_range(value, intervals.get_wind_speed(), False),  # Скорость ветра, м/с
        'precipitation': lambda value: f.to_binary_range(value, intervals.precipitation(), False),  # Осадки, мм
        'daylight': lambda value: f.to_binary_equal(value, intervals.daylight(), False),  # Естественное освещение
        'straight_stripes_project': lambda value: f.to_binary_equal(value, intervals.lanes_according_plan(), False),
        # Фактическое количество полос в прямом направлении
        'straight_lanes_provided': lambda value: f.to_binary_equal(value, intervals.lanes_according_plan(), False),
        # Обеспечиваемое количество полос в прямом направле-нии
        'lanes_left': lambda value: f.to_binary_equal(value, intervals.number_of_lanes_per_turn(), False),
        # Количество дополнительных полос для поворота нале-во
        'lanes_right': lambda value: f.to_binary_equal(value, intervals.number_of_lanes_per_turn(), False),
        # Количество дополнительных полос для поворота напра-во
        'left_stripe_view': lambda value: f.to_binary_equal(value, intervals.turn_lane_view(), False),
        # Вид дополнительной полосы для поворота налево: 0 - с основной; 1 - карман; 0.1 - вариан
        'right_stripe_view': lambda value: f.to_binary_equal(value, intervals.turn_lane_view(), False),
        # Вид дополнительной полосы для поворота направо: 0 - с основной; 1 - карман; к - канализир. движ.
        'strip_length_left': lambda value: f.to_binary_range(value, intervals.caraman_length(), False),
        # Длина дополнительной полосы для поворота налево
        # "0 if np.isnan(value) else value" - если нет  значений, то ячейка =0
        'strip_length_right': lambda value: f.to_binary_range(value, intervals.caraman_length(), False),
        # Длина дополнительной полосы для поворота направо
        # "0 if np.isnan(value) else value" - если нет  значений, то ячейка =0
        'type_movement': lambda value: f.to_binary_equal(value, intervals.type_of_traffic(), False),
        # Вид дорожного движения на рассматриваемом участке (одностороннее 1, двухстороннее - 2)
        'distance_to_parking': lambda value: f.to_binary_range(value, intervals.distance_to_parking(), False),
        # Расстояние до парковки от рубежа контроля по ходу движения автомобиля
        'method_of_setting': lambda value: f.to_binary_equal(value, intervals.type_and_method_of_parking(), False),
        # Вид постановки автомобиля на парковку (фактический), (0, 1, 2, 3)
        'type_of_parking': lambda value: f.to_binary_equal(value, intervals.type_and_method_of_parking(), False),
        # Вид парковки (0, 1, 2)
        'longitudinal_slope': lambda value: f.to_binary_range(value, intervals.ascent_and_descent(), False),
        # Продольный уклон (за 100 м до контр. участ) ‰
        'dead_end_street': lambda value: [value],  # Выезд с тупиковой улицы
        'total_strip_width': lambda value: f.to_binary_range(value, intervals.design_road_width(), False),
        # Суммарная ширина полос для движения одном направ-лении (с учетом дополнительных полос для поворотов)
        'tota_forward_direction_width': lambda value: f.to_binary_range(value, intervals.design_road_width(), False),
        # Суммарная ширина полос для движения в одном направлении (без дополнительных полос для поворотов)
        'narrowing_of_movement': lambda value: f.to_binary_range(value, intervals.design_road_width(), False),
        # Сужение прямого направления за 100 метров до рубежа контроля
        # # 'Широта': lambda value: f.to_binary_range(value, intervals   ???????
        # # 'Долгота': lambda value: f.to_binary_range(value, intervals   ???????
        'dividing_strip': lambda value: f.to_binary_equal(value, intervals.direction_separator(), False),
        # Разделительная полоса
        'Area': lambda value: f.to_binary_equal(value, intervals.area(), False),  # Район г. Хабаровска
        'distance_to_bus_stop': lambda value: f.to_binary_range(value, intervals.distance_to_bus_stop(), False),
        # Расстояние до конца автобусной остановки по ходу движения;
        'bus_stop_type': lambda value: f.to_binary_equal(value, intervals.bus_stop_type(),
                                                         intervals.intersection_type(), False),
        # Тип автобусной остановки (0 - без кармана, 1- карман)
        'traffic_light_regulation': lambda value: [value]  # Светофорное регулирование (0- нет, 1- есть)
    }

    def dataframe_to_dict(df):
        result = dict()
        for column in df.columns:
            values = data_frame[column].values
            result[column] = values
        return result
    def make_supervised(df):
        raw_input_data = data_frame[input_names]
        raw_output_data = data_frame[output_names]
        return {"inputs": dataframe_to_dict(raw_input_data),
                "outputs": dataframe_to_dict(raw_output_data)}

    def encode(data):
        vectors = []
        for data_name, data_values in data.items():
            encoded = list(map(encoders[data_name], data_values))
            vectors.append(encoded)
        formatted = []
        for vector_raw in list(zip(*vectors)):
            vector = []
            for element in vector_raw:
                for e in element:
                    vector.append(e)
            formatted.append(vector)
        return formatted

    def predict(prediction_d, real_d, name_csv):
        intensivity_groups = [
            "0...250", "251...500", "501...750", "751...1000",
            "1001...1250", "1251...1500", "1501...1750", "1751...2000",
            "2001...2250", "2251...2500", "2501...2750", "2751...3000",
            "3001...3250", "3251...3500", "3501...3750", "3751...4000",
            "4001...4250", "4251...4500", "4501...4750", "4751...5000",
            "5001...100000000"]
        pr = prediction_d.tolist()
        outputs = []
        for v in pr:
            max_value = max(v)
            max_index = v.index(max_value)
            outputs.append(intensivity_groups[max_index])
        real_d['ИнтенсивностьДиапазон'] = outputs
        real_d.to_csv(name_csv, sep=";", encoding="utf-8-sig")
        return True

    model = k.Sequential()  # Создаем модель
    supervised = make_supervised(data_frame)
    encoded_inputs = np.array(encode(supervised["inputs"]))
    # 2-й шаг - тренируем модель либо загружаем ее
    if need_train:
        encoded_outputs = np.array(encode(supervised["outputs"]))
        model.add(k.layers.Dense(units=200, activation="relu"))  # todo: сделать по количеству колонок
        model.add(k.layers.Dense(units=150, activation="relu"))
        model.add(k.layers.Dense(units=21, activation="sigmoid"))
        model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
        """В процентном отношени делим данные на обучение и на валидацию (проверку обучения)"""
        data_division = round(
            len(data_frame) * 0.97)  # Считаем количество строк, выбираем из них 60%, записываем получившееся количество и округляем
        print("Всего", len(data_frame), "строк, из них ", data_division, "идет на обучение, а ",
              len(data_frame) - data_division, " на тест")

        train_x = encoded_inputs[:data_division]  # todo: брать не конкретное число а процент массива
        train_y = encoded_outputs[:data_division]
        test_x = encoded_inputs[data_division:]
        test_y = encoded_outputs[data_division:]
        fit_results = model.fit(x=train_x, y=train_y, epochs=200, validation_split=0.2, shuffle=True)
        prediction_data = model.predict(test_x)
        real_data = data_frame.iloc[data_division:][input_names + output_names]
        predict(prediction_data, real_data,
                os.getcwd() + '/output/trained/' + filename + '.csv')  # предсказанные тестовые данные

        results = model.evaluate(test_x, test_y,
                                 # batch_size=128
                                 )
        with open(os.getcwd() + '/output/results.txt', 'a') as h:
            h.seek(0, 2)  # перемещение курсора в конец файла
            h.write(filename + ': test loss, test acc:' + str(results) + "\n")
        """"Записываем каждый результат в csv файл"""
        model.save(os.getcwd() + '/output/models/' + filename + '.model.h5')
        print('Модель обучена, запустите программу еще раз!')
        return True
    else:
        predict_x = encoded_inputs
        model = k.models.load_model(os.getcwd() + '/output/models/' + filename + '.model.h5')
        prediction_data = model.predict(predict_x)
        real_data = data_frame[input_names]
        predict(prediction_data, real_data, os.getcwd() + '/output/predicted/' + filename + '.csv')
