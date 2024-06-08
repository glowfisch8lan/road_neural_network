import portion as P
from app.domain.helpers import types
import math

COLUMN_NAME = 'strip_length_left' # Длина дополнительной полосы для поворота налево


def validate(value):
    if math.isnan(value):
        value = -1 # ЭТО ЗНАЧИТ НЕТ ЛЕВОЙ ПОЛОСЫ
    r1 = P.closed(-1, 300)
    types.is_float(float(value), "Left_pocket_length_Validator") # Проверяем на целочисленный тип
    types.in_range(value, r1, "Left_pocket_length_Validator")
    return value

