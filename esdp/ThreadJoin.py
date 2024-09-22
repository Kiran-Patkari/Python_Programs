from threading import*
class MyThread:
    def run(self):
        for x in range(1,11):
            print("Child Thread")
m=MyThread()
t=Thread(target=m.run)
t.start()
t.join()
for x in range(1,11):
    print("Main Thread")