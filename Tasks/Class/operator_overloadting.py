#OPERATOR OVERLOADING
#Operator overloading - giving to the extra behaviour of existing operator
# function overloading - 
# method overloadting - *args, **kwargs

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def display(self):
#         print(self.name, self.marks)
#     def __add__(self,other):
#         return self.marks+other
#     def info(self):
#         pass
# s=Student('rama',30)
# s.info()#--Requirement, we dont want name
# s=Student(30)
# s1=Student(40)
# print(s+s1)

#example of operator overloading
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(self.name, self.marks)
    def __add__(self,other):
        return self.marks+other
s=Student('rama',30)
s1=Student('ravi',40)
s.display()
s1.display()
s2=s+s1
print(s2)
#example of operator overloading