import portion as P
from app.domain.helpers import types
import math

COLUMN_NAME = 'lanes_left' # Количество дополнительных полос для поворота нале-во


def validate(value):
    if math.isnan(value):
        value = 0
    types.is_int(int(value), "Lanes_left_Validator")
    types.in_range(value, [0, 0.5, 1, 2], "Lanes_left_Validator")
    return value