import portion as P
from app.domain.helpers import types
COLUMN_NAME = 'saturation_deficit' # Дефицит насыщения (d), г/м³
def validate(value):
    r1 = P.closed(0, 40)
    types.is_float(value, "SaturationValidator")
    types.in_range(value, r1, "SaturationValidator")
    return value
