#activity1

class Car:
    brand = "Toyota" 

    def add_car(self, number_plate):
        self.number_plate = number_plate  
car1 = Car()
car2 = Car()

car1.add_car("TN01AB1234")
car2.add_car("KA05CD5678")

print(car1.brand, car1.number_plate)
print(car2.brand, car2.number_plate)

