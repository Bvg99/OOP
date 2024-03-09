class Vehicle:
    vehicle_type = None

class Car:
    price = 1000000

    def horse_powers(self, horse_of_powers):
        return horse_of_powers

class Nissan(Vehicle, Car):
    vehicle_type = 'diesel'
    price = 1500000
    def horse_powers(self, horse_of_powers):
        return horse_of_powers

car = Car()
print('car:', car.price, car.horse_powers(120))

vehicle = Vehicle()
print('vehicle:', vehicle.vehicle_type, car.horse_powers(250))

nissan = Nissan()
print('nissan:', nissan.vehicle_type, nissan.price, nissan.horse_powers(265))
