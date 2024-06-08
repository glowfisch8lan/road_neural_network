import portion as P
from app.domain.helpers import types
import math

COLUMN_NAME = 'strip_length_right' # Длина дополнительной полосы для поворота направо


def validate(value):
    if math.isnan(value):
        value = -1 # ЭТО ЗНАЧИТ НЕТ ЛЕВОЙ ПОЛОСЫ
    r1 = P.closed(-1, 300)
    types.is_float(float(value), "Right_pocket_length_Validator")
    types.in_range(value, r1, "Right_pocket_length_Validator")
    return value

