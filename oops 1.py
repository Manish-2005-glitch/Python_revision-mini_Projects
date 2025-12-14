from car import Car

car1 = Car("MUSTANG", 2025, "Black", False)
car2 = Car("M3", 2024, "Blue", True)
car3 = Car("Defender", 2023, "White", True)
print(car2.color)
car1.drive()
car3.stop()
print(car1.wheel)
car2.describe()
car3.describe()
print(Car.wheel)

print(Car.num_cars)