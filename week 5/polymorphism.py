# Base Class
class Vehicle:
    def move(self):
        pass

# Subclasses with polymorphism
class Car(Vehicle):
    def move(self):
        print(" Car is driving on the road.")

class Plane(Vehicle):
    def move(self):
        print(" Plane is flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print(" Boat is sailing in the ocean.")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()