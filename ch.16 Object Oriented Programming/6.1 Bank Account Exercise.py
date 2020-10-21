#Define class called BankAccount
# Each BankAccount should have an owner
#-- Specified when a new BankAccount is created BankAccount("Charlie")
#-- Each BankAccount should have a balance attribute (Starts out with 0.0)
# Each instance should have a deposit method, accepts number and adds to balance
#- then return new balance
#Each instance should have a withdraw method, accepts number and subtracts from balance
#- then return new balance

class BankAccount: #class
    def __init__(self, name):
        self.owner = name
        self.balance = 0.0

    def getBalance(self): #method (fnc of the class)
        return self.balance
    def deposit(self, deposit):
        self.balance += deposit #put self.balance first to save it in the variable
        return self.balance
    def withdraw(self,withdraw):
        self.balance -= withdraw
        return self.balance

acct = BankAccount("Darcy") #Object (instances of the class)
print (acct.owner)