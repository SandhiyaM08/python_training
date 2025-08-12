#activity3
#create a vehicle base class and two subclass with overridden methods


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        return self.brand

    def stop(self):
        return self.brand

class Car(Vehicle):
    def start(self):
        return self.brand

class Motorcycle(Vehicle):
    def start(self):
        return self.brand

car = Car("Toyota", "Camry")
bike = Motorcycle("Yamaha", "R15")

print(car.start())       
print(bike.start())     
print(car.stop())        
