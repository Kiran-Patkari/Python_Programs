class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        
    def work(self):
        print("Work in progress-")

    def getsalary(self,salary):
        self.salary=salary

      

class HRManager(Employee):
    def work():
        print("--Override work function--")

    def addEmployee(self):
        print()




