import os

from app.predictor import start as predict

for file in os.listdir(os.getcwd() + '/output/validated'):
    split = os.path.splitext(file)
    filename = split[0]
    predict(need_train=True, filename=filename)


