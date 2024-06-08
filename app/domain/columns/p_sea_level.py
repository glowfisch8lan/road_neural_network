import portion as P
from app.domain.helpers import types
COLUMN_NAME = 'pressure_sea' # Атмосферное давление на уровне моря (P моря), г.Па
def validate(value):
    r1 = P.closed(900, 1100)
    types.is_float(value, "p_sea_levelValidator")
    types.in_range(value, r1, "p_sea_leveValidator")
    return value
