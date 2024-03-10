class Car:
    price = 1000000
    horse_of_powers = None

    def __init__(self, name):
        self.name = name

    def horse_powers(self, engine_volume):          # вводим объем двигателя
        self.horse_of_powers = engine_volume * 100  # в функции вычисляем мощность
        return self.horse_of_powers                 # возвращаем значение мощности


class Nissan(Car):
    price = 1500000

    def horse_powers(self, engine_volume):
        # переопределяем функцию (изменяем формулу для вычисления мощности)
        self.horse_of_powers = engine_volume * 100 + self.price / 100000
        return self.horse_of_powers


class Kia(Car):
    price = 2000000

    def horse_powers(self, engine_volume):
        self.horse_of_powers = engine_volume * 100 - self.price / 100000
        return self.horse_of_powers


car = Car('Car')
car_horse_of_powers = car.horse_powers(1.5)
print('name:', car.name, ' price:', car.price, ' horse of powers:',
      car_horse_of_powers)

nissan = Nissan('Nissan')
nissan_horse_of_powers = nissan.horse_powers(2)
print('name:', nissan.name, ' price:', nissan.price, ' horse of powers:',
      nissan_horse_of_powers)

kia = Kia('Kia')
kia_horse_of_powers = kia.horse_powers(2.5)
print('name:', kia.name, ' price:', kia.price, ' horse of powers:',
      kia_horse_of_powers)