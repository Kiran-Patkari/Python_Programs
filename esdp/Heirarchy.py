class A:
    def display():
        print("Display of first parent")
class B:
    def display1():
        print("Display of second parent")
class C(A,B):
    def display2():
        print("Display of child")

c=C()
c.display()
c.display1()
c.display2()

