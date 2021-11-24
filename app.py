class Category: 
    ledger = []
    
    def __init__(self):
        self.balance = 0
    
    def deposit(self, amount, description):
        if (type(amount) == int or type(amount) == float) and amount > 0:
            ledger_item = {"amount": amount, "description": description}
            Category.ledger.append(ledger_item)
            self.balance += amount
            print("Deposit Successful")
        else:
            print("[!] Error! Invalid input")
            
    def withdraw(self, amount, description):
        if (type(amount) == int or type(amount) == float) and amount > 0 and self.check_funds(amount) == True:
            ledger_item = {"amount": 0 - amount, "description": description}
            Category.ledger.append(ledger_item)
            self.balance -= amount
            print("Withdraw Successful")
        else:
            print("[!] Error! Invalid input or not enough funds")
    
    def transfer(self, amount, budget_category):
        if (type(amount) == int or type(amount) == float) and amount > 0 and self.check_funds(amount) == True:
            self.withdraw(amount, "Transfer from" + self)
            budget_category.deposit(amount, "Transfer to" + budget_category)
            print("Transfer Successful")
            return True
        else:
            print("[!] Error! Something went wrong")
            return False
            
    def check_funds(self, amount):
        if self.balance < amount:
            return False
        else:
            return True
