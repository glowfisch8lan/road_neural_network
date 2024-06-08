import portion as P
from app.domain.helpers import types
import math

COLUMN_NAME = 'distance_to_bus_stop'# Расстояние до конца автобусной остановки по ходу движения


def validate(value):
    if math.isnan(value):
        value = -1 # ЭТО ЗНАЧИТ НЕТ ЛЕВОЙ ПОЛОСЫ
    r1 = P.closed(-1, 2000)
    types.is_float(float(value), "Distance_to_bus_stop_Validator")
    types.in_range(value, r1, "Distance_to_bus_stop_Validator")
    return value

