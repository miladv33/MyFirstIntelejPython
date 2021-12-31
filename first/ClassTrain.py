class User:
    def __init__(self, thing):
        self.thing = thing

    def whatIsTheThing(self):
        return self.thing


user = User(12)
print(user.thing)

happy = User("milad")
print(happy.thing)

print(happy.whatIsTheThing())


def somthing(num: int):
    print(num)


somthing("fdf")
