class Sample:
    def display1(self):
        print("Display of Sample")
class Demo(Sample):
    def display2(self):
        print("Display of Demo")
d=Demo()
d.display1()
d.display2()