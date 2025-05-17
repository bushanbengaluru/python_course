#example of inheritance hierarchy
class A:
    def display(self):
        print("This is class A")
class B(A):
    def out(self):
        print("This is class B")
class C():
    def display(self):
        print("This is class C")
class D(C):
    def out(self):
        print("This is class D")

a = A()
b = B()
c = C()
d = D()
d.display()