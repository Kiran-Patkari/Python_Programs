class Outer:
     def __init__(self):
          print("Outer class object creation")
     class Inner:
         def __init__(self):
               print("Inner class object creation")
         def func(self):
               print("This is inner class method")


o=Outer()
i=o.Inner()
i.func()
print('~'*30)
i1.Outer().Inner()
i1.func()


