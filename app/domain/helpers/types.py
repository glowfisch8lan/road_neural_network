from app.domain.helpers import logger


def is_int(value, validator):
    if type(value) is not int:
        logger.fail(validator + ' Error in cell - incorrect value - not int : ' + str(value))
        raise Exception("validator error")


def is_float(value, validator):
    if type(value) is not float:
        logger.fail(validator + ' Error in cell - incorrect value - not float : ' + str(value))
        raise Exception("validator error")


def in_range(value, r1, validator):
    if value not in r1:
        logger.fail(validator + ': Error in cell - incorrect value not in range: ' + str(value))
        raise Exception("validator error. Значение не в диапазоне " + str(value))
