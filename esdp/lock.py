from threading import*
import time
l=Lock()
def play(name):
    l.acquire()
    for i in range(10):
      print("Batting:",name)
      time.sleep(1)
    l.release()

t1=Thread(target=play,args=("Sachin",))
t2=Thread(target=play,args=("Yuvraj",))
t3=Thread(target=play,args=("Kohli"))

t1.start()
t2.start()
t3.start()




