from threading import*
class MyThread:
    def rum(self):
        for x in range(1,11):
            print("Child Thread")
m=MyThread()
t=Thread(target=m.run)
t.start()
for x in range(1,11):
    print("Main Thread")