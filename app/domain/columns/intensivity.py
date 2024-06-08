import portion as P
from app.domain.helpers import types
COLUMN_NAME = 'intensity' # Интенсивность
def validate(value):
    r1 = P.closed(0, float('inf'))
    types.is_int(value, "IntensivityValidator")
    types.in_range(value, r1, "IntensivityValidator")
    return value
