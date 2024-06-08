from app.domain.helpers import types
import math
import app.domain.helpers.utils as f
COLUMN_NAME = 'daylight' #Естественное освещение
def validate(value):
    if 0.5 < value < 1:
        value = float(f.toFixed(value, 2))
    types.in_range(value, [0, 0.5, 0.85, 1], "Daylight_Validator")
    return value
