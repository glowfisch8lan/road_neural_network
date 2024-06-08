from app.domain.helpers import types
import math


COLUMN_NAME = 'straight_stripes_project' # Фактическое количество полос в прямом направлении

def validate(value):
    types.is_int(int(value), "lanes_according_plan_Validator")
    types.in_range(value, [0, 1, 2, 3, 4, 5], "lanes_according_plan_Validator")
    return value
