

class Transport:
    def __init__(self, name):
        self.name = name

    def description(self):
        return f"Транспорт - {self.name}"


class Car(Transport):
    def __init__(self, name, horsepower):
        super().__init__(name)
        self.horsepower = horsepower

    def description(self):
        return f"Машина - {self.name} | Лошадиные силы - {self.horsepower}"


class Plane(Transport):
    def __init__(self, name, vehicle_capacity):
        super().__init__(name)
        self.vehicle_capacity = vehicle_capacity

    def description(self):
        return f"Самолет - {self.name} | Максимальная вместимость - {self.vehicle_capacity}"


class Bike(Transport):
    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed

    def description(self):
        return f"Байк - {self.name} | Максимальная скорость - {self.speed}"


def print_info(object: Transport):
    return object.description()

toyota = Car("Toyota", 200)
airbus = Plane("Airbus A305", 150)
yamaha = Bike("Yamaha MT-09", 240)

print(print_info(toyota))
print(print_info(airbus))
print(print_info(yamaha))

