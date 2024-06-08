import portion as P
from app.domain.helpers import types
import math

COLUMN_NAME = 'method_of_setting' # Вид постановки автомобиля на парковку (фактический), (0, 1, 2, 3)


def validate(value):
    if math.isnan(value):
        value = -1 # ЭТО ЗНАЧИТ НЕТ ПРАВОЙ ПОЛОСЫ
    types.is_int(int(value), "Type_and_method_of_parking_Validator")
    types.in_range(value, [0, 1, 2, -1], "Type_and_method_of_parking_Validator")
    return value