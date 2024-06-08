import portion as P
from app.domain.helpers import types
COLUMN_NAME = 'dead_end_street' #Выезд с тупиковой улицы
def validate(value):
    types.is_int(int(value), "Dead_end_street_Validator")
    types.in_range(value, [0, 1], "Dead_end_street_Validator")
    return value