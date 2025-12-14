class Car:

    wheel = 4 #class variable defined outside tthe constructor but shared among all objects
    num_cars = 0
    def __init__(self, model, year, color, for_sale):
        self.model = model #instance variable these are defined inside the constructor.
        self.year = year
        self.color = color
        self.for_sale = for_sale
        Car.num_cars += 1

    #Methods

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.model}, {self.year}, {self.color}")