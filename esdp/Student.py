
class Student:
    
    def accept(self,name,rolln):
        self.name=name
        self.rolln=rolln

    def display(self):
        print("Name:",self.name)
        print("Rollno",self.rolln)

name=input("Enter name:")
rolln=int(input("Enter rollno:"))



s=Student()
s.accept(name,rolln)
s.display()

    

    

