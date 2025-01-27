class BankAccount:
    
    def __init__(self, owner, balance=0):
        self.owner=owner
        self.balance=balance
    
    def deposit(self,amount):
        if amount > 0:
            self.ba;lance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        
        else:
            print("deposit amount must be positive.")
        
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else: 
            print("Funds need to be added.")
            
    def get_balance(self):
        return self.balance

    account = BankAccount("Julia", 250)

    account.deposit(50)
    account.withdraw(70)
    print("Final Balance:", account.get_balance())