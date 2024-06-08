from app.domain.helpers import types
import math
COLUMN_NAME = 'visibility_VV' # Видимость, шифр (VV);
def validate(value):
    if math.isnan(value):
        value = 0
    types.is_int(int(value), "VisibilityValidator")
    types.in_range(value, [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 0], "VisibilityValidator")
    return value
