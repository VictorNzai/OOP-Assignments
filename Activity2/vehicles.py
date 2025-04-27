class Vehicle:
    def move(self):
        pass  # this is the Abstract method

class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing across the water 🚤")

# Using Polymorphism
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()
