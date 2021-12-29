def myPrinter(name):
    print(f'hello {name}')


myPrinter('john')


def number(num, plus):
    return num + plus


print(number(1, 2))

# lambda

getsum = lambda myAge, yourAge: myAge + yourAge

print(getsum(10, 20))
