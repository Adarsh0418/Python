class Emp:
    college_name = 'SJBIT'
    def __init__(self, name):
        self.name = name

e1 = Emp('Akash')
e2 = Emp('Anikit')

# class level variable can be accessed using object reference or class Name:
print(e1.college_name)
print(e2.college_name)
print(Emp.college_name)

'''
class level variable are such variables which are declares inside the class and outside any
method.
All objects for that class shares same copy of class variables.

Instance variabes are such variables which are present insisde objects.
For each object sepeste copy of instance 
'''