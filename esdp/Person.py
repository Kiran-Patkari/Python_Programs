class Person:
    #name="Krishna"
    #village="Dhule"
    #job="photographer"

    def accept(self,name,village,job):
        self.name=name
        self.village=village
        self.job=job

    def display(self):
        print("Name:",self.name)
        print("Village:",self.village)
        print("Job",self.job)

name=input("Enter your name:")
village=input("Enter your village:")
job=input("Enter your job:")

p=Person()
p.accept(name,village,job)

