class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType


    def __eq__(self, other):
        return (self.numberOfFloors == other.numberOfFloors
                and self.buildingType == other.buildingType)


industrial_building = Building(12, 'industrial')
residential_building = Building(25, 'residential')

print('industrial_building: floors ', industrial_building.numberOfFloors, ',  type ', industrial_building.buildingType)
print('residential_building: floors ', residential_building.numberOfFloors, ',  type ', residential_building.buildingType)

if industrial_building == residential_building:
    print('no different. for what was rebuilt?')
else:
    print('thats better')