from MyFirstModule import printAHello
from camelcase import CamelCase
from datetime import date
from time import time

today = date.today()
print(today)
print(time())

camelcase = CamelCase
# print("{}", camelcase.hump('hello there world'))
printAHello()
