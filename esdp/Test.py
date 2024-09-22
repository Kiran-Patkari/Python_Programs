class Test:
    def sum(self,*n):
        total=0
        for x in n:
            total=total+x
        print("Sum=",total)

t=Test()
t.sum(10,20)
t.sum(10,20,30)
t.sum(10,20,30,40)
t.sum(10)
t.sum()