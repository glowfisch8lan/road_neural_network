from app.domain.helpers import types
import math


COLUMN_NAME = 'traffic_light_regulation' # Светофорное регулирование (0- нет, 1- есть)

def validate(value):
    if math.isnan(value):
        value = 0
    types.is_int(int(value), "Traffic_light_Validator")
    types.in_range(value, [0, 1], "Traffic_light_Validator")
    return value
