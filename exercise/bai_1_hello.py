print("Lam chu python trong 4 tuan")
print("Ham print trong python tuong tu ham printf trong C")


class Car:
    num = 4

    def __init__(self):
        self.color = "while"
        self.style = "sedan"
        self.speed = 45

    def change_color(self, color):
        self.color = color

    def change_style(self, style):
        self.style = style

    def change_speed(self, speed):
        self.speed = speed


class FuelCar(Car):
    def __init__(self, fuel_type):
        super().__init__()
        self.fuel_type = fuel_type

    def change_fuel_type(self):
        self.fuel_type = "oil"


class ElectricCar(Car):
    pass


myCar = Car()
myCar.change_speed(100)
myCar.change_color("black")
print(myCar.color, myCar.style, myCar.speed, myCar.num)



