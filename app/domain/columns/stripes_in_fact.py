from app.domain.helpers import types
import math


COLUMN_NAME = 'straight_stripes_project' # Фактическое количество полос в прямом направлении

def validate(value):
    types.is_int(int(value), "stripes_in_fact_Validator")
    types.in_range(value, [0, 1, 2, 3, 4, 5], "stripes_in_fact_Validator")
    return value
