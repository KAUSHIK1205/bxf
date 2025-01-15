class Car:
    def __init__(self, mileage, model):
        self.mileage = mileage
        self.model = model

class BMW(Car):
    def info(self, model):
        self.model = model
        self.mileage = 250  # Setting mileage for BMW M3

    def print(self):
        print(f"BMW {self.model} with mileage {self.mileage} km/h")

class FERRARI(Car):
    def info(self, model):
        self.model = model
        self.mileage = 340  # Setting mileage for Ferrari 488 GTB

    def print(self):
        print(f"Ferrari {self.model} with mileage {self.mileage} km/h")

b = BMW(0, '')  # Initializing with default values
b.info('M3')
b.print()

f = FERRARI(0, '')  # Initializing with default values
f.info('488 GTB')
f.print()




              
        



