"""6. Bank Account with Transaction History
Each transaction is its own object — stored inside the Account.
▲ Hide 
Create a Transaction class with type ("deposit"/"withdrawal"), amount, and date."""
from datetime import datetime
class Transaction:
    def __init__(self, ttype, amount, date):
        self.ttype = ttype
        self.amount = amount
        self.date = date
        
"""Create a BankAccount class with owner, balance, and a list of Transaction objects."""
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.transactions = []
        
    """Add deposit(amount) and withdraw(amount) methods — each creates a Transaction and appends it."""
    def deposit(self, amount):
        self.balance += amount
        transaction = Transaction("Deposit", amount, datetime.now())
        self.transactions.append(transaction)
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            transaction = Transaction("Withdrawal", amount, datetime.now())
            self.transactions.append(transaction)
        else:
            print("Transaction Error!")
        
    
    """Add a statement() method that prints all transactions and the final balance."""
    def statement(self):
        print("***Transaction details ***")
        print(f"Name: {self.owner}")
        print("----------------------------")
        print(f"Balance: {self.balance}")
        
        for t in self.transactions:
            print(f"Date: {t.date.strftime('%Y-%m-%d %H:%M:%S')} | Status: {t.ttype} | Amount: ${t.amount}")
            
        print("_________________________")
        print(f"Final Balance: ${self.balance}")      
        
account1 = BankAccount("Harry Bruce", 50000)

account1.deposit(10000)
account1.withdraw(2000)
account1.withdraw(58001)
account1.statement()

"""output of the above py file:
Transaction Error!
***Transaction details ***
Name: Harry Bruce
----------------------------
Balance: 58000
Date: 2026-02-26 14:23:49 | Status: Deposit | Amount: $10000
Date: 2026-02-26 14:23:49 | Status: Withdrawal | Amount: $2000
_________________________
Final Balance: $58000

=== Code Execution Successful ==="""


    
    
