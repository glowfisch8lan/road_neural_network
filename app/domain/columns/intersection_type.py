import portion as P
from app.domain.helpers import types
import math

COLUMN_NAME = 'Intersection_type' # Тип перекрестка (т, у, х, 0, ж)

def validate(value):
    if value == "т":
        value = 1
    elif value == "у":
        value = 2
    elif value == "х":
        value = 3
    elif value == "ж":
        value = 4
    else:
        value = -1

    types.is_int(int(value), "Intersection_type_Validator")
    types.in_range(value, [1, 2, 3, 4, -1], "Intersection_type_Validator")
    return value