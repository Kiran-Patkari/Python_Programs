import gc
#import 
#import

class Time:
   def __init__(self):
      print("Constructor is called")
   def _del__(self):
      print("Desctructor is called")

t=Time()
t=None
print("Application is ended")
#destructor used for destroying objects

