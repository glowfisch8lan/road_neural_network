import portion as P
from app.domain.helpers import types
import math

COLUMN_NAME = 'distance_to_parking'# Расстояние до парковки от рубежа контроля по ходу движения автомобиля


def validate(value):
    if math.isnan(value):
        value = float(-1)
    r1 = P.closed(-1, 150)
    types.is_float(value, "Distance_to_parking_Validator")
    types.in_range(value, r1, "Distance_to_parking_Validator")
    return value
