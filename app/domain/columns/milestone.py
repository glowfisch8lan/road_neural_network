import portion as P
from app.domain.helpers import types
import math

COLUMN_NAME = 'frontier' # Рубеж


def validate(value):
    r1 = P.closed(0, 10000)
    types.in_range(value, r1, "Milestone_Validator")
    return value
