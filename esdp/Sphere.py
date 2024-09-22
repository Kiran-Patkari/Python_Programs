class Sphere:
    def __init__(self,pi,rad):
        self.pi=pi
        self.rad=rad

    def cal(self):

        area=4*pi*rad*rad
        print("surfacearea:",self.area)
        volume=(4/3)*pi*rad*rad*rad
        print("volume:",self.volume)


pi=float(input("Enter value of pi:"))
rad=float(input("Enter value of rad:"))
s=Sphere(pi,rad)
s.cal()