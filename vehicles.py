class Car:
    def __init__(self, id, color, mspd, acc, stpt, enpt):
        self.id = id
        self.color = color
        self.mspd = mspd
        self.acc = acc
        self.stpt = stpt
        self.enpt = enpt

class Bus(Car):
    def __init__(self, id, color, mspd, acc, stpt, enpt, route):
        super().__init__(id, color, mspd, acc, stpt, enpt)
        self.route = route