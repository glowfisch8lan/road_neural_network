import portion as P
from app.domain.helpers import types
import math

COLUMN_NAME = 'right_stripe_view' # Вид дополнительной полосы для поворота направо: 0 - с основной; 1 - карман; к - канализир. движ.


def validate(value):
    if math.isnan(value):
        value = -1 # ЭТО ЗНАЧИТ НЕТ ПРАВОЙ ПОЛОСЫ
    types.is_int(int(value), "Right_turn_view_Validator")
    types.in_range(value, [0, 0.1, 1, -1], "Right_turn_view_Validator")
    return value