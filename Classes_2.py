class House:
    def __init__(self):
        self.number_of_floors = 10


    def lift(self):
        for current_floor in range(1, 11):
            print('current floor: ', current_floor)

house = House()
house.lift()