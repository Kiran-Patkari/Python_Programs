class Date:
    def __init__(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year
    def display(self):
        print("Day:",self.day)
        print("Month:",self.month)
        print("Year:",self.year)

day=int(input("Enter Date: "))
month=int(input("Enter Month: "))
year=int(input("Enter Year: "))

d= Date(day,month,year)
d.display() 

        
