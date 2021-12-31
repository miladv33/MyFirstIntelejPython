class Hama:
    def __init__(self, miner):
        self.miner = miner


class User:
    def __init__(self, thing):
        self.thing = thing

    def whatIsTheThing(self):
        return self.thing


class Customer(User, Hama):

    def __init__(self):
        self.thing = ""
        self.miner = 12
