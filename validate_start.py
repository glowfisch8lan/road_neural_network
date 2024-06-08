import os

from app.validator import start as validate

for file in os.listdir(os.getcwd() + '/output/r'):
    split = os.path.splitext(file)
    filename = split[0]
    validate(True, filename)
