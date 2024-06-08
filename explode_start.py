import os
import pandas as pd

df = pd.read_csv(os.getcwd() + '/dataset.csv', sep=";")
n = df.groupby('frontier') #Сортруем по рубежам
grp_idx = n.groups
for key in grp_idx.keys():
    r = n.get_group(key)
    #r.drop(columns=r.columns[0], axis=1, inplace=True)  # убираем лишний столбец
    #r.drop(columns=r.columns[16], axis=1, inplace=True)  # убираем лишний столбец
    r.to_csv(os.getcwd() + '/output/r/' + str(key) + '.csv', sep=";", encoding="utf-8-sig")