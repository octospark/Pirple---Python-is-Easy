import random

class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.NeedsMaintenance = False
        self.TripsSinceMaintenance = 0

    # getters
    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getYear(self):
        return self.year

    def getWeight(self):
        return self.weight

    # setters
    def setMake(self, make):
        self.make = make

    def setModel(self, model):
        self.model = model

    def setYear(self, year):
        self.year = year

    def setWeight(self, weight):
        self.weight = weight

    def Repair(self):
        if self.NeedsMaintenance:
            self.NeedsMaintenance = False
            self.TripsSinceMaintenance = 0

        
class Car(Vehicle):
    def __init__(self, make, model, year, weight, isDriving):
        Vehicle.__init__(self, make, model, year, weight)
        self.isDriving = isDriving

    def Drive(self):
        if not self.isDriving:
            self.TripsSinceMaintenance += 1
            self.isDriving = True
        if self.TripsSinceMaintenance == 100:
            self.NeedsMaintenance = True

    def Stop(self):
        if self.isDriving:
            self.isDriving = False



class Planes(Vehicle):
    def __init__(self, make, model, year, weight, isFlying):
        Vehicle.__init__(self, make, model, year, weight)
        self.isFlying = isFlying

    def Flying(self):
        if not self.isFlying:
            if self.TripsSinceMaintenance == 100:
                self.NeedsMaintenance = True
                print("Cant fly plane before undergoing a maintenance")
            else:
                self.TripsSinceMaintenance += 1
                if self.TripsSinceMaintenance == 100:
                    self.NeedsMaintenance = True
                self.isFlying = True
            

    def Landing(self):
        if self.isFlying:
            self.isFlying = False
        
        
            

def DriveCar(car):
    '''Produce a random number of trips for a given car'''
    for i in range(random.randint(1, 150)):
        car.Drive()
        car.Stop()

def GetState(car):
    '''Print a human friendly message with all the relevant data
    of a given car'''
    if car.NeedsMaintenance:
        maintenanceMessage = " needs maintenance "
    else:
        maintenanceMessage = " doesn't need maintenance "
        
    message = car.getMake() + ", " + car.getModel() + " produced in " + \
              str(car.getYear()) + " weighing " + str(car.getWeight())+ "kg " + \
              maintenanceMessage + " after " + \
              str(car.TripsSinceMaintenance) + " trips."
    return message


car1 = Car("Audi", "Q7", 2016, 2400, False)
car2 = Car("Benz Mercedes", "C-Class", 2017, 2070, False)
car3 = Car("BMW", "X6", 2014, 2340, False)

DriveCar(car1)
DriveCar(car2)
DriveCar(car3)

print(GetState(car1))
print(GetState(car2))
print(GetState(car3))

plane = Planes("Piper", "Cherokee 235", 1964, 710, False)

for i in range(105):
    if i > 95:
        print("Trip number", plane.TripsSinceMaintenance, "Does plane need maintenance? ", plane.NeedsMaintenance)
    plane.Flying()
    plane.Landing()
        
