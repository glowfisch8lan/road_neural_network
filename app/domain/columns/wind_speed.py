import portion as P
from app.domain.helpers import types
import math
COLUMN_NAME = 'wind_speed' # Скорость ветра, м/с
def validate(value):
    if math.isnan(value):
        value = float(0)
    r1 = P.closed(0, 40)
    types.is_float(value, "Wind_speedValidator")
    types.in_range(value, r1, "Wind_speedValidator")
    return value
