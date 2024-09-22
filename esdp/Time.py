class Time:
    def __init__(self,hour,min,sec):
        self.hour=hour
        self.min=min
        self.sec=sec
    def show(self):
        print("Hour:",self,hour)
        print("Min:",self,min)
        print("Sec:",self,sec)
    
hour=input("Enter Hour:")
min=input("Enter min:")
sec=input("Enter sec:")

t1=Time(hour,min,sec)
t1.show()

