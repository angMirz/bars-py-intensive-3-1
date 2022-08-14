class Multiplier:
    def __init__(self, value):
        value = self.value

    def get_value(self):
        return self.value

    def __add__(self, secondValue):
        return self.value + secondValue.get_value()

    def __sub__(self, secondValue):
        return self.value - secondValue.get_value()

    def __mul__(self, secondValue):
        return self.value * secondValue.get_value()

    def __truediv__(self, secondValue):
        return self.value / secondValue.get_value()

    def __floordiv__(self, secondValue):
        return self.value // secondValue.get_value()

class Hundred(Multiplier):
    def __init__(self, value):
        self.value = value * 100


class Thousand(Multiplier):
    def __init__(self, value):
        self.value = value * 1000


class Million(Multiplier):
    def __init__(self, value):
        self.value = value * 1000000


a = Hundred(10).get_value()

b = Thousand(2).get_value()

print(b//a)