import portion as P
from app.domain.helpers import types
COLUMN_NAME = 't_dew_point' # Температура точки росы (DP), С°
def validate(value):
    r1 = P.closed(-100, 100)
    types.is_float(value, "TDewValidator")
    types.in_range(value, r1, "TDewValidator")
    return value
