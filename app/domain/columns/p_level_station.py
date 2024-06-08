import portion as P
from app.domain.helpers import types
COLUMN_NAME = 'pressure_station' # Атмосферное давление на уровне станции (P станции), г.Па
def validate(value):
    r1 = P.closed(900, 1100)
    types.is_float(value, "p_level_stationValidator")
    types.in_range(value, r1, "p_level_stationValidator")
    return value
