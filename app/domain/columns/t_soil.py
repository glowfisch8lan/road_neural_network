import portion as P
from app.domain.helpers import types
COLUMN_NAME = 't_soil' # Температура почвы (t почвы), С°
def validate(value):
    r1 = P.closed(-100, 100)
    types.is_float(value, "TSoilValidator")
    types.in_range(value, r1, "TSoilValidator")
    return value
