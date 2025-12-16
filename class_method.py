class Student:
    
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return f"{self.name} = {self.gpa}"

    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"The average gpa of the students are: {cls.total_gpa/cls.count:.2f}"

student1 = Student("Manish", 2)
student2 = Student("Nisha", 3.6)
student3 = Student("P", 1.5)
print(Student.count)
print(Student.get_avg_gpa())

    