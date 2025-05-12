# class
class superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def display(self):
        print(f"{self.name} and was born in {self.origin}")
    def use_power(self):
        print(f"{self.name} uses {self.power} power to lift heavy objects")
    
    # inheritance
class flying_superhero(superhero):
    def __init__(self, name, power, origin, flight_speed):
        self.flight_speed = flight_speed
        super().__init__(name, power, origin)

    def use_power(self):
        print(f"{self.name} flies through the sky at {self.flight_speed} speed using their {self.power} power")

# creating an object
superhero1 = superhero("Superman", "super strength", "Krypton")
superhero1.display()
superhero1.use_power()

flying_superhero1 = flying_superhero("Iron Man", "flight", "Earth", 1000)
flying_superhero1.display()
flying_superhero1.use_power()
