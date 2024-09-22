from threading import *
print(current_thread().getName())
current_thread().setName("RCPIT")
print(current_thread().getName())