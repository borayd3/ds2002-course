#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3


import os

os.environ["FAV_ANIMAL"] = input('What is your favorite animal? ')

os.environ["STATE"] = input('What state are you from? ')

os.environ["CLASS_NUM"] = input('How many classes are you taking this semester? ')

print(os.getenv("FAV_ANIMAL"))
print(os.getenv("STATE"))
print(os.getenv("CLASS_NUM"))
