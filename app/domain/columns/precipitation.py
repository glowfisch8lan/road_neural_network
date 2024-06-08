import portion as P
from app.domain.helpers import types
import math
COLUMN_NAME = 'precipitation' # Осадки, мм
def validate(value):
    if math.isnan(value):
        value = float(0)
    r1 = P.closed(0, 100)
    types.is_float(value, "Precipitation_Validator")
    types.in_range(value, r1, "Precipitation_Validator")
    return value
