class Building:
    def __init__(self):
        self.numberOfFloors = 12
        self.buildingType = 'industrial'

    def rebuilt(self):
        print('building has rebuilt')
        self.numberOfFloors = 25
        self.buildingType = 'residential'

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors


industrial_building = Building()
residential_building = Building()
another_residential_building = Building()

print('floors: ', industrial_building.numberOfFloors, ',  type: ', industrial_building.buildingType)

residential_building.rebuilt()

print('floors: ', residential_building.numberOfFloors, ',  type: ', residential_building.buildingType)

if industrial_building == residential_building:
    print('no different. for what was rebuilt?')
else:
    print('thats better')