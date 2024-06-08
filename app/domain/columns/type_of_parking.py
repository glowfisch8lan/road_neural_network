import portion as P
from app.domain.helpers import types
import math

COLUMN_NAME = 'type_of_parking' # Вид парковки (0, 1, 2)


def validate(value):
    if math.isnan(value):
        value = -1 # ЭТО ЗНАЧИТ НЕТ паковки рядом
    types.is_int(int(value), "Type_of_parking_Validator")
    types.in_range(value, [0, 1, 2, -1], "Type_of_parking_Validator")
    return value