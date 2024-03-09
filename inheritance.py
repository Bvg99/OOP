class Car:
    price = 1000000
    wheels = 4

    def __init__(self, name):
        self.name = name

    def horse_powers(self, horse_of_powers):
        return horse_of_powers


class Nissan(Car):
    price = 1500000

    def horse_powers(self, horse_of_powers):
        return horse_of_powers


class Kia(Car):
    price = 2000000

    def horse_powers(self, horse_of_powers):
        return horse_of_powers


car = Car('Car')
car_horse_of_powers = car.horse_powers(150)
print('name:', car.name, ' price:', car.price, ' horse of powers:',
      car_horse_of_powers, 'wheels:', car.wheels)

# price и horse_of_powers переопределены, wheels берётся из родительского класса

nissan = Nissan('Nissan')
nissan_horse_of_powers = nissan.horse_powers(220)
print('name:', nissan.name, ' price:', nissan.price, ' horse of powers:',
      nissan_horse_of_powers, 'wheels:', nissan.wheels)

kia = Kia('Kia')
kia_horse_of_powers = kia.horse_powers(280)
print('name:', kia.name, ' price:', kia.price, ' horse of powers:',
      kia_horse_of_powers, 'wheels:', kia.wheels)