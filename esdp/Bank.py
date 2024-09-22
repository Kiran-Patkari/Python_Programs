class Bank:
    def __init__(self):
        self.depositor=" "
        self.accno=" "
        self.tyacc=" "
        self.balamount=0
        
    def inputData(self):
        self.depositor=input("Enter name of depoditor:")
        #accno=int(input("Enter accout no:"))
        #yacc=input("Enter type of account")
        self.balamount=eval(input("Enter balance amount:"))
        self.amount=eval(input("Enter deposit Amount :"))

    def deposit(self):
        #self.amount=amount  
        self.balamount+=self.amount
        print("Balance_Amount after deposit:",self.balamount)

    def widraw(self):
        if self.amount>self.balamount:
            print("Insufficient Balance:")
        else:
            self.balamount-=self.amount
            print("After Widraw balance is:",self.balamount)

    def display(self):
        print("Name of customer:",self.depositor)
        print("Balance amount:",self.balamount)

b=Bank()
b.inputData()
b.deposit()
b.widraw()
b.display()



        

        
            

        
