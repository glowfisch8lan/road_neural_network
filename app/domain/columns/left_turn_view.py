import portion as P
from app.domain.helpers import types
import math

COLUMN_NAME = 'left_stripe_view' # Вид дополнительной полосы для поворота налево: 0 - с основной; 1 - карман; 0.1 - варианта


def validate(value):
    if math.isnan(value):
        value = -1 # ЭТО ЗНАЧИТ НЕТ ЛЕВОЙ ПОЛОСЫ
    types.is_int(int(value), "Left_turn_view_Validator")
    types.in_range(value, [0, 0.1, 1, -1], "Left_turn_view_Validator")
    return value