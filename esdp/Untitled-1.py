class Bank:
    def __init__(self):
        self.depositor=0
        self.accno=0
        self.tyacc=0
        self.balamount=0
        
    def inputData(self):
        depositor=input()
        accno=int(input())
        tyacc=input()
        balamount=eval(input())
    

    def deposit(self,amount):
        self.amount=amount
        self.balamount+=amount
        print("Balance_Amount after deposit:",self.balamount)

    def widraw(self):
        if self.amount>self.balamount:
            print("Insufficient Balance:")
        else:
            self.balamount-=self.amount
            print("After Widraw balance is:",self.balamount)

    def display(self):
        print("Name of customer:",self.name)
        print("Balance amount:",self.balamount)

b=Bank()
b.inputData()
b.deposit(50,000)
b.widraw()
b.display()



        

        
            

        
