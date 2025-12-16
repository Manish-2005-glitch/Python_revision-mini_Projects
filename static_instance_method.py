class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Janitor", "Coder", "Cook", "Laundry"]
        return position in valid_positions

employee1 = Employee("Nisha", "Coder")
employee2 = Employee("Manish", "Janitor")
employee3 = Employee("Priyambada", "Cook")

print(Employee.is_valid_position("Janitor"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
