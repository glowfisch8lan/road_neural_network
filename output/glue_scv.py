import glob
import pandas as pd

path = 'trained'
filenames = glob.glob(path + "\*.csv")
dfs = []
for filename in filenames:
    tmp = pd.read_csv(filename, sep=";")
    tmp['frontier'] = filename
    dfs.append(tmp)
    # line.insert(loc=0, column='player', value=filename)
big_frame = pd.concat(dfs, ignore_index=True)
big_frame.to_csv('general.csv', sep=";", encoding="utf-8-sig")
