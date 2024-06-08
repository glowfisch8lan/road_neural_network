import portion as P
from app.domain.helpers import types
COLUMN_NAME = 'humidity' # Относительная влажность воздуха (ϕ), %;
def validate(value):
    r1 = P.closed(-100, 110)
    types.is_float(value, "FPercentValidator")
    types.in_range(value, r1, "FPercentValidator")
    return value
