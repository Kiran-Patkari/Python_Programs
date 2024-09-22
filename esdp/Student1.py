class Student1:
    def __init__(self):
        self.name=" "
        self.rollno=" "
        self.address=" "
        self.per=0

    def accept(self):
        self.namer =input("Enter your name:")
        self.rollno=int(input("Enter your rollno:"))
        self.address=input("Enter your address:")
        self.per=float(input("Enter your percentage:"))

    def display(self):
        if self.per>=70:
            print("Destinction")
        elif self.per<70 and self.per>=68:
            print("First Class")
        elif self.per<60 and self.per>=40:
            print("Second Class")
        elif self.per<40:
            print("Student is fail--")
        else:
            print("Invalid")

s=Student1()
s.accept()
s.display()
