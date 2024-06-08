import os
import pandas as pd
from sklearn.ensemble import IsolationForest
"""Изолированный лес"""
def cleaner(filename):
    data_frame = pd.read_csv(os.getcwd() + "/../output/validated/" + filename + ".csv", delimiter=";")  # подгружаем файл
    data_frame.drop(columns=data_frame.columns[0], axis=1, inplace=True)  # убираем лишний столбец
    # data_frame.info()
    """Изолированный лес"""
    model = IsolationForest(n_estimators=50, max_samples='auto', contamination=float(0.1), max_features=1.0)
    model.fit(data_frame[['intensity']])
    data_frame['scores_intensity'] = model.decision_function(data_frame[['intensity']])
    data_frame['anomaly_intensity'] = model.predict(data_frame[['intensity']])
    return data_frame
for file in os.listdir(os.getcwd() + '/../output/validated'):
    split = os.path.splitext(file)
    filename = split[0]
    print(filename)
    data_frame = cleaner(filename=filename)
    data_frame.to_csv(os.getcwd() + '/../output/validated/' + filename + '.csv', sep=";", encoding='utf-8-sig')