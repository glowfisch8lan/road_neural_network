import portion as P
from app.domain.helpers import types
import math

COLUMN_NAME = 'dividing_strip' # Разделительная полоса


def validate(value):
    if math.isnan(value):
        value = -1 # ЭТО ЗНАЧИТ НЕТ паковки рядом
    types.is_int(int(value), "Traffic_separator_Validator")
    types.in_range(value, [0, 1, 2, -1], "Traffic_separator_Validator")
    return value