import portion as P
from app.domain.helpers import types
import math

COLUMN_NAME = 'longitudinal_slope' # Продольный уклон (за 100 м до контр. участ) ‰


def validate(value):
    if math.isnan(value):
        value = 0
    r1 = P.closed(-150, 150)
    types.is_float(float(value), "Ascent_Validator")
    types.in_range(value, r1, "Ascent_Validator")
    return value


