class BankAccount:
    def __init__(self,balance=0):
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print("New Balance:",self.balance)
        else:
            print("Invalid deposit amount")

    def withdraw(self,amount):
        if amount>0 and self.balance>=amount:
            self.balance-=amount
            print("After withdraw balance is:",self.balance)
        else:
            print("Invalid withdraw value")

class SavingsAccount(BankAccount):
    def withdraw(self,amount):
        if self.balance-amount>=1000:
            super().withdraw(amount)
        else:
            print("withdraw is not possible due to insufficient balance")

def main():
    account=SavingsAccount()

    while True:
         print("--Menu--/")
         print("1. Deposit")
         print("2. Withdraw")
         print("3. Exit")

         choice=input("Enter your choice:")
         if choice==1:
            amount=float(input("Enter Deposit amount:"))
            account.deposit(amount)
         elif choice==2:
            amount=float(input("Enter Withdraw amount: "))
            account.withdraw(amount)
         elif choice==3:
            print("Exist the program")
            break
         else:
            print("Invalid choice ")

if __name__== "__main__":
   main()





        

    
             
        