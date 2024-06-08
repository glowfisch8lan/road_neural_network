import portion as P
from app.domain.helpers import types
COLUMN_NAME = 'partial_pressure' # Парциальное давление водяного пара (ps), Па
def validate(value):
    r1 = P.closed(0, float('inf'))
    types.is_float(value, "PressureValidator")
    types.in_range(value, r1, "PressureValidator")
    return value
