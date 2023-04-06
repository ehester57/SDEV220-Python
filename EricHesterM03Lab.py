class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type):
        super().__init__(vehicle_type)
        self.year = None
        self.make = None
        self.model = None
        self.doors = None
        self.roof = None

    def properties(self, year, make, model, doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def __str__(self):
        return f"Vehicle type: {self.vehicle_type}\n"\
               f"Year: {self.year}\n"\
               f"Make: {self.make}\n"\
               f"Model: {self.model}\n"\
               f"Number of doors: {self.doors}\n"\
               f"Type of roof: {self.roof}\n"
    
vehicle_type = "car"

car = Automobile(vehicle_type)

car.year = input("Enter the year: ")
car.make = input("Enterthe make: ")
car.model = input("Enter the model: ")
car.doors = input("Enter the number of doors (2 or 4): ")
car.roof = input("Enter the type of roof (solid or sunroof): ")

print("\nHere is the information you entered:\n")
print(car)
