from threading import*
class MyThread(Thread):
    def rum(self):
        for x in range(1,11):
            print("Child Thread")
m=MyThread()
m.start()
for x in range(1,11):
    print("Main Thread")