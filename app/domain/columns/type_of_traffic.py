from app.domain.helpers import types
import math


COLUMN_NAME = 'type_movement' # Вид дорожного движения на рассматриваемом участке (одностороннее 1, двухстороннее - 2)

def validate(value):
    types.is_int(int(value), "Type_of_traffic_Validator")
    types.in_range(value, [1, 2], "Type_of_traffic_Validator")
    return value
