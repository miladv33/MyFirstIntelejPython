from MyFirstModule import printAHello
from camelcase import CamelCase
from datetime import date
from time import time

# today = date.today()
# print(today)
# print(time())

camelcase = CamelCase


# print("{}", camelcase.hump('hello there world'))
# printAHello()

# strBinary = str(bin(2)[2:])
# binary = bin(int(strBinary))
# deci = int(binary, 2)
# print(deci)


def flippingBits(n):
    n = bin(n)[2:]
    n = str(n)
    n = n.replace("1", "2")
    n = n.replace("0", "1")
    n = n.replace("2", "0")
    remain32 = 32 - len(n)
    while remain32 > 0:
        n = str(n)
        n = "".join(f"1{n}")
        remain32 -= 1
    n = int(n, 2)
    return n


print(flippingBits(0))
