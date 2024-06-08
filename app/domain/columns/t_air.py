import portion as P
from app.domain.helpers import types
COLUMN_NAME = 't_air' #Температура воздуха (t воздуха), С°
def validate(value):
    r1 = P.closed(-100, 100)
    types.is_float(value, "TAirValidator")
    types.in_range(value, r1, "TAirValidator")
    return value
