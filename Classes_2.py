class House:
    def __init__(self):
        self.number_of_floors = 10


    def lift(self):
        for current_floor in range(self.number_of_floors + 1):
            print('current floor: ', current_floor)

house = House()
house.lift()