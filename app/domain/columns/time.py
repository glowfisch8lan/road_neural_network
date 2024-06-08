import portion as P
from app.domain.helpers import types
COLUMN_NAME = 'day_time' # Время суток
def validate(value):
    r1 = P.closed(0, 23)
    types.is_int(value, "TimeValidator")
    types.in_range(value, r1, "TimeValidator")
    return value
