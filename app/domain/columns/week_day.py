import portion as P
from app.domain.helpers import types
COLUMN_NAME = 'week_day' # День недели
def validate(value):
    r1 = P.closed(1, 7)
    types.is_int(value, "WeekValidator")
    types.in_range(value, r1, "WeekValidator")
    return value
