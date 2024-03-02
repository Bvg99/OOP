class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floor):
        self.numberOfFloors = floor
        print(self.numberOfFloors)


house = House()

house.setNewNumberOfFloors(18)