import portion as P
from app.domain.helpers import types
import numpy as np

COLUMN_NAME = 'Area' # Район

def validate(value):
    if value == "ц":
        value = np.int64(1)
    elif value == "к":
        value = np.int64(2)
    elif value == "и":
        value = np.int64(3)
    elif value == "ж":
        value = np.int64(4)
    else:
        raise Exception("Validator error area. Значение неизвестно" + str(value))

    types.is_int(int(value), "Area_Validator")
    types.in_range(value, [1, 2, 3, 4], "Area_separator_Validator")
    return value