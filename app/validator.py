import os
from app.domain.columns import names_input
from app.domain.columns import names_output
from app.domain.columns import validators as get_validators
from app.domain.helpers import logger
import pandas as pd
def start(need_train, filename):
    # 1-й шаг - готовим данные
    data = pd.read_csv(os.getcwd() + '/output/r/'+filename+'.csv', sep=';')
    validators = get_validators()
    new_array = dict()
    for data_name, data_values in data.items():
        if data_name in validators:
            l = validators[data_name]
            s = data_values
            encoded = list(map(l, s))
            new_array[data_name] = encoded
            logger.success('`' + str(data_name) + '`' + ' validated success!')
    df = pd.DataFrame(new_array)
    if need_train:
        d = names_input() + names_output()
    else:
        d = names_input()
    df.to_csv(os.getcwd() + '/output/validated/'+filename+'.csv', sep=";",
              columns=d, encoding='utf-8-sig')

