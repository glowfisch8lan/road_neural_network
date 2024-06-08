import portion as P
from app.domain.helpers import types
import math
COLUMN_NAME = 'bus_stop_type' #Тип автобусной остановки (0 - без кармана, 1- карман)
def validate(value):
    if math.isnan(value):
        value = -1 # ЭТО ЗНАЧИТ НЕТ автобусной остановки
    types.is_int(int(value), "Bus_stop_type_Validator")
    types.in_range(value, [0, 1, -1], "Bus_stop_type_Validator")
    return value

