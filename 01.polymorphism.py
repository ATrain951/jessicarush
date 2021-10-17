# Base Vehicle:
class Vehicle:
    # Constructor
    def __init__(self, owner): 
        self.owner = owner
         
    def get_owner(self):
        return self.owner 
        
    # Methods in which every subclass will be required to implement.
    def top_speed(self):
        raise NotImplementedError("Subclass is missing it's top speed method.")   


# Vehicles:
class Truck(Vehicle):
    def top_speed(self):
        return "The truck has a top speed of 120mph."
      

class Sedan(Vehicle):
    def top_speed(self):
        return "The sedan has a top speed of 140mph."
   
        
class SportsCar(Vehicle):
    def top_speed(self):
        return "The sportscar has a top speed of 200mph."


vehicles = [
    Truck("Chris"),
    Sedan("Kyle"),
    Sedan("Justin"),
    SportsCar("John"),
]

for vehicle in vehicles:
    print(vehicle.get_owner())
    print(" * " + str(vehicle.top_speed()))
    
    
    
    
"""
Chris
 * The truck has a top speed of 120mph.
Kyle
 * The sedan has a top speed of 140mph.
Justin
 * The sedan has a top speed of 140mph.
John
 * The sportscar has a top speed of 200mph.
"""
