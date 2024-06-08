import portion as P
from app.domain.helpers import types
import math

COLUMN_NAME = 'lanes_right' # Количество дополнительных полос для поворота напра-во


def validate(value):
    if math.isnan(value):
        value = 0
    types.is_int(int(value), "Lanes_right_Validator")
    types.in_range(value, [0, 0.5, 1, 2], "Lanes_right_Validator")
    return value