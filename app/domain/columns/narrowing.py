import math

import portion as P
from app.domain.helpers import types

COLUMN_NAME = 'narrowing_of_movement' # Сужение прямого направления за 100 метров до рубежа контроля


def validate(value):
    if math.isnan(value):
        value = -1 # ЭТО ЗНАЧИТ НЕТ прямого направления
    r1 = P.closed(-1, 70)
    types.in_range(value, r1, "Narrowing_Validator")
    return value
