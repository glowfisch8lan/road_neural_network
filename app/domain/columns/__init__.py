# день недели
from app.domain.columns.week_day import validate as week_validator
from app.domain.columns.week_day import COLUMN_NAME as WEEK_COLUMN_NAME
#   Время суток
from app.domain.columns.time import COLUMN_NAME as TIME_COLUMN_NAME
from app.domain.columns.time import validate as time_validator
#   Интенсивность
from app.domain.columns.intensivity import COLUMN_NAME as INTENSIVE_COLUMN_NAME
from app.domain.columns.intensivity import validate as intensive_validator
#   Температура воздуха
from app.domain.columns.t_air import COLUMN_NAME as T_AIR_COLUMN_NAME
from app.domain.columns.t_air import validate as t_air_validator
#   Температура почвы
from app.domain.columns.t_soil import COLUMN_NAME as T_SOIL_COLUMN_NAME
from app.domain.columns.t_soil import validate as t_soil_validator
#   Температура точки росы
from app.domain.columns.t_dew import COLUMN_NAME as T_DEW_COLUMN_NAME
from app.domain.columns.t_dew import validate as t_dew_validator
# Парциальное давление водяного пара (ps), Па
from app.domain.columns.pressure import COLUMN_NAME as PRESSURE_COLUMN_NAME
from app.domain.columns.pressure import validate as pressure_validator
# Относительная влажность воздуха (ϕ), %;
from app.domain.columns.f_percent import COLUMN_NAME as F_PERCENT_COLUMN_NAME
from app.domain.columns.f_percent import validate as f_percent_validator
# Видимость, шифр (VV);
from app.domain.columns.visibility_cipher import COLUMN_NAME as VISIBILITY_CIPHER_COLUMN_NAME
from app.domain.columns.visibility_cipher import validate as visibility_cipher_validator
# Дефицит насыщения (d), г/м³
from app.domain.columns.saturation_deficit import COLUMN_NAME as SATURATION_DEFICIT_COLUMN_NAME
from app.domain.columns.saturation_deficit import validate as saturation_deficit_validator
# Атмосферное давление на уровне станции (P станции), г.Па
from app.domain.columns.p_level_station import COLUMN_NAME as P_LEVEL_STARION_COLUMN_NAME
from app.domain.columns.p_level_station import validate as p_level_station_validator
# Атмосферное давление на уровне моря (P моря), г.Па
from app.domain.columns.p_sea_level import COLUMN_NAME as P_SEA_LEVEL_COLUMN_NAME
from app.domain.columns.p_sea_level import validate as p_sea_level_validator
# Погода, шифр (ww)
from app.domain.columns.weather_code_ww import COLUMN_NAME as WEATHER_CODE_WW_COLUMN_NAME
from app.domain.columns.weather_code_ww import validate as weather_code_ww_validator
#Направление ветра, градусы
from app.domain.columns.direction_wind import COLUMN_NAME as DIRECTION_WIND_COLUMN_NAME
from app.domain.columns.direction_wind import validate as direction_wind_validator
# Скорость ветра, м/с
from app.domain.columns.wind_speed import COLUMN_NAME as WIND_SPEED_COLUMN_NAME
from app.domain.columns.wind_speed import validate as wind_speed_validator
# Осадки, мм
from app.domain.columns.precipitation import COLUMN_NAME as PRECIPITATION_COLUMN_NAME
from app.domain.columns.precipitation import validate as precipitation_validator
#Естественное освещение
from app.domain.columns.daylight import COLUMN_NAME as DAYLIGHT_COLUMN_NAME
from app.domain.columns.daylight import validate as daylight_validator

from app.domain.columns.lanes_according_plan import COLUMN_NAME as LANES_ACCORDING_COLUMN_NAME
from app.domain.columns.lanes_according_plan import validate as lanes_according_plan_validator

from app.domain.columns.stripes_in_fact import COLUMN_NAME as STRIPES_IN_FACT_COLUMN_NAME
from app.domain.columns.stripes_in_fact import validate as stripes_in_fact_validator
#
from app.domain.columns.lanes_left import COLUMN_NAME as LANES_LEFT_COLUMN_NAME
from app.domain.columns.lanes_left import validate as lanes_left_validator

from app.domain.columns.lanes_right import COLUMN_NAME as LANES_RIGHT_COLUMN_NAME
from app.domain.columns.lanes_right import validate as lanes_right_validator

from app.domain.columns.left_turn_view import COLUMN_NAME as LEFT_TURN_VIEW_COLUMN_NAME
from app.domain.columns.left_turn_view import validate as left_turn_view_validator

from app.domain.columns.right_turn_view import COLUMN_NAME as RIGHT_TURN_VIEW_COLUMN_NAME
from app.domain.columns.right_turn_view import validate as right_turn_view_validator

from app.domain.columns.left_pocket_length import COLUMN_NAME as LEFT_POCKET_LENGTH_COLUMN_NAME
from app.domain.columns.left_pocket_length import validate as left_pocket_length_validator

from app.domain.columns.right_pocket_length import COLUMN_NAME as RIGHT_POCKET_LENGTH_COLUMN_NAME
from app.domain.columns.right_pocket_length import validate as right_pocket_length_validator

from app.domain.columns.type_of_traffic import COLUMN_NAME as TYPE_OF_TRAFFIC_COLUMN_NAME
from app.domain.columns.type_of_traffic import validate as type_of_traffic_validator
#
from app.domain.columns.distance_to_parking import COLUMN_NAME as DISTANCE_TO_PARKING_COLUMN_NAME
from app.domain.columns.distance_to_parking import validate as distance_to_parking_validator

from app.domain.columns.type_and_method_of_parking import COLUMN_NAME as TYPE_AND_METHOD_OF_PARKING_COLUMN_NAME
from app.domain.columns.type_and_method_of_parking import validate as type_and_method_of_parking_validator

from app.domain.columns.type_of_parking import COLUMN_NAME as TYPE_OF_PARKING_COLUMN_NAME
from app.domain.columns.type_of_parking import validate as type_of_parking_validator

from app.domain.columns.longitudinal_slope import COLUMN_NAME as ASCENT_COLUMN_NAME
from app.domain.columns.longitudinal_slope import validate as ascent_validator

from app.domain.columns.dead_end_street import COLUMN_NAME as DEAD_END_STREET_COLUMN_NAME
from app.domain.columns.dead_end_street import validate as dead_end_street_validator

from app.domain.columns.width_project import COLUMN_NAME as WIDTH_PROJECT_COLUMN_NAME
from app.domain.columns.width_project import validate as width_project_validator

from app.domain.columns.straight_direction_only_width import COLUMN_NAME as STRAIGHT_DIRECTION_ONLY_WIDTH_COLUMN_NAME
from app.domain.columns.straight_direction_only_width import validate as straight_direction_only_width_validator
#
from app.domain.columns.narrowing import COLUMN_NAME as NARROWING_COLUMN_NAME
from app.domain.columns.narrowing import validate as narrowing_validator

from app.domain.columns.traffic_separator import COLUMN_NAME as TRAFFIC_SEPARATOR_COLUMN_NAME
from app.domain.columns.traffic_separator import validate as traffic_separator_validator

from app.domain.columns.area import COLUMN_NAME as AREA_COLUMN_NAME
from app.domain.columns.area import validate as area_validator

from app.domain.columns.distance_to_bus_stop import COLUMN_NAME as DISTANCE_TO_BUS_STOP_COLUMN_NAME
from app.domain.columns.distance_to_bus_stop import validate as distance_to_bus_stop_validator

from app.domain.columns.bus_stop_type import COLUMN_NAME as BUS_STOP_TYPE_COLUMN_NAME
from app.domain.columns.bus_stop_type import validate as bus_stop_type_validator

from app.domain.columns.intersection_type import COLUMN_NAME as INTERSECTION_TYPE_COLUMN_NAME
from app.domain.columns.intersection_type import validate as intersection_type_validator
#
from app.domain.columns.traffic_light import COLUMN_NAME as TRAFFIC_LIGHT_COLUMN_NAME
from app.domain.columns.traffic_light import validate as traffic_light_validator

from app.domain.columns.milestone import COLUMN_NAME as MILESTONE_COLUMN_NAME
from app.domain.columns.milestone import validate as milestone_validator

import app.domain.helpers.utils as f
import app.domain.helpers.intervals as intervals

# Колонки по порядку
_columns_inputs = [
    WEEK_COLUMN_NAME, # День недели
    TIME_COLUMN_NAME, #   Время суток
    T_AIR_COLUMN_NAME,#   Температура воздуха
    T_SOIL_COLUMN_NAME,#   Температура почвы
    T_DEW_COLUMN_NAME,#   Температура точки росы
    PRESSURE_COLUMN_NAME,# Парциальное давление водяного пара (ps), Па
    F_PERCENT_COLUMN_NAME,# Относительная влажность воздуха (ϕ), %;
    VISIBILITY_CIPHER_COLUMN_NAME,# Видимость, шифр (VV);
    SATURATION_DEFICIT_COLUMN_NAME,# Дефицит насыщения (d), г/м³
    P_LEVEL_STARION_COLUMN_NAME,# Атмосферное давление на уровне станции (P станции), г.Па
    P_SEA_LEVEL_COLUMN_NAME,# Атмосферное давление на уровне моря (P моря), г.Па
    WEATHER_CODE_WW_COLUMN_NAME,# Погода, шифр (ww)
    DIRECTION_WIND_COLUMN_NAME,#Направление ветра, градусы
    WIND_SPEED_COLUMN_NAME,# Скорость ветра, м/с
    PRECIPITATION_COLUMN_NAME,# Осадки, мм
    DAYLIGHT_COLUMN_NAME,# Естественное освещение

    # MILESTONE_COLUMN_NAME,
    # LANES_ACCORDING_COLUMN_NAME,
    # STRIPES_IN_FACT_COLUMN_NAME,
    # LANES_LEFT_COLUMN_NAME,
    # LANES_RIGHT_COLUMN_NAME,
    # LEFT_TURN_VIEW_COLUMN_NAME,
    # RIGHT_TURN_VIEW_COLUMN_NAME,
    # LEFT_POCKET_LENGTH_COLUMN_NAME,
    # RIGHT_POCKET_LENGTH_COLUMN_NAME,
    # TYPE_OF_TRAFFIC_COLUMN_NAME,
    # DISTANCE_TO_PARKING_COLUMN_NAME,
    # TYPE_AND_METHOD_OF_PARKING_COLUMN_NAME,
    # TYPE_OF_PARKING_COLUMN_NAME,
    # ASCENT_COLUMN_NAME,
    # DEAD_END_STREET_COLUMN_NAME,
    # WIDTH_PROJECT_COLUMN_NAME,
    # STRAIGHT_DIRECTION_ONLY_WIDTH_COLUMN_NAME,
    # NARROWING_COLUMN_NAME,
    # TRAFFIC_SEPARATOR_COLUMN_NAME,
    # AREA_COLUMN_NAME,
    # DISTANCE_TO_BUS_STOP_COLUMN_NAME,
    # BUS_STOP_TYPE_COLUMN_NAME,
    # INTERSECTION_TYPE_COLUMN_NAME,
    # TRAFFIC_LIGHT_COLUMN_NAME,
]
_columns_outputs = [INTENSIVE_COLUMN_NAME]

# Валидаторы по порядку
_validators_input = [
    week_validator,# День недели
    time_validator,#   Время суток
    t_air_validator,#   Температура воздуха
    t_soil_validator,#   Температура почвы
    t_dew_validator,#   Температура точки росы
    pressure_validator,# Парциальное давление водяного пара (ps), Па
    f_percent_validator,# Относительная влажность воздуха (ϕ), %;
    visibility_cipher_validator,# Видимость, шифр (VV);
    saturation_deficit_validator,# Дефицит насыщения (d), г/м³
    p_level_station_validator,# Атмосферное давление на уровне станции (P станции), г.Па
    p_sea_level_validator,# Атмосферное давление на уровне моря (P моря), г.Па
    weather_code_ww_validator,# Погода, шифр (ww)
    direction_wind_validator,#Направление ветра, градусы
    wind_speed_validator,# Скорость ветра, м/с
    precipitation_validator,# Осадки, мм
    daylight_validator,# Естественное освещение
    #milestone_validator,
    # lanes_according_plan_validator,
    # stripes_in_fact_validator,
    # lanes_left_validator,
    # lanes_right_validator,
    # left_turn_view_validator,
    # right_turn_view_validator,
    # left_pocket_length_validator,
    # right_pocket_length_validator,
    # type_of_traffic_validator,
    # distance_to_parking_validator,
    # type_and_method_of_parking_validator,
    # type_of_parking_validator,
    # ascent_validator,
    # descent_validator,
    # dead_end_street_validator,
    # width_project_validator,
    # straight_direction_only_width_validator,
    # narrowing_validator,
    # traffic_separator_validator,
    # area_validator,
    # distance_to_bus_stop_validator,
    # bus_stop_type_validator,
    # intersection_type_validator,
    # traffic_light_validator
 ]
_validators_output = [intensive_validator]


# Колонки names_input которые использовать в анализе данных
def names_input():
    return _columns_inputs
def names_output():
    return _columns_outputs
# Получить список колонка-валидатор
def validators():
    return dict(zip(_columns_inputs+_columns_outputs,
                    _validators_input+_validators_output))




