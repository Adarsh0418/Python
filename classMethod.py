class Stuent:
    college_name = 'ABC University"' \
    
    def __init__(self, name, age, roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number

    @classmethod
    def change_college_name(cls,new_name):
        cls.change_college_name = new_name

    def attend_class(self):
        print(f"{self.name} from {Stuent.college_name} is attending the class.")

Student.change_college_name("XYZ University")

student_1 = Stuent('Amit', 20, '$123')
student_2 = Stuent('Priya', 22, '$124')
