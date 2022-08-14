class MathClock:
    def __init__(self):
        self.hours = 0
        self.minutes = 0

    def __add__(self, value):
        self.minutes += value

        if (self.minutes > 60):
            self.hours += 1
            self.minutes -= 60
            if (self.hours > 23):
                self.hours = 0

    def __sub__(self, value):
        self.minutes -= value

        if (self.minutes < 0):
            self.hours -= 1
            self.minutes = 60 + self.minutes
            if (self.hours < 0):
                self.hours = 23

    def __mul__(self, value):
        self.hours += value 
        if (self.hours > 23):
            self.hours = self.hours % 24
    
    def __truediv__(self, value):
        self.hours -= value 
        if (self.hours < 0):
            self.hours = 24 + ( -(-(self.hours) % 24)  if self.hours < -24  else self.hours)

    def get_time(self):
        return f'{str(self.hours).zfill(2)} : {str(self.minutes).zfill(2)}'

clock = MathClock()
clock + 50
clock + 20
clock - 30
print(clock.get_time())
clock / 50
print(clock.get_time())

