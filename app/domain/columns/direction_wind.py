import portion as P
from app.domain.helpers import types
COLUMN_NAME = 'wind_direction' #Направление ветра, градусы
def validate(value):
    r1 = P.closed(0, 360)
    types.is_float(value, "direction_windValidator")
    types.in_range(value, r1, "direction_windValidator")
    return value
