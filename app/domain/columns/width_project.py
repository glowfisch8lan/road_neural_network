import portion as P
from app.domain.helpers import types

COLUMN_NAME = 'total_strip_width' # Суммарная ширина полос для движения одном направ-лении (с учетом дополнительных полос для поворотов)


def validate(value):
    r1 = P.closed(0, 70)
    types.is_float(value, "Width_project_Validator")
    types.in_range(value, r1, "Width_project_Validator")
    return value
