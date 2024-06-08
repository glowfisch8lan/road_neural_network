import portion as P
from app.domain.helpers import types
import math
COLUMN_NAME = 'tota_forward_direction_width' # Суммарная ширина полос для движения в одном направлении (без дополнительных полос для поворотов)


def validate(value):
    if math.isnan(value):
        value = -1 # ЭТО ЗНАЧИТ НЕТ прямого направления
    r1 = P.closed(-1, 70)
    types.in_range(value, r1, "Straight_direction_only_width_Validator")
    return value
