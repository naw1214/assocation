class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    # your code here! (remember, instance attributes go here)
    # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else: 
            print('You have insuffcient funds')
            self.balance -= 5
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    
    def display_account_info(self):
        return f'{self.balance}'
    
    @classmethod
    def print_info(cls):
        for account in cls.accounts:
            account.display_account_info()

class User:		# here's what we have so far
    def __init__(self, name): # makes the instance of the class
        self.name = name
        self.account = BankAccount(.05,1000) # instance of BankAccount
    def display_user_balance(self):
        print(f'User: {self.name}, Balance: {self.account.display_account_info()}')
        return self

    def transfer(self,amount,user):
        self.account_balance -= amount
        user.account_balance += amount
        self.display_user_balance()
        user.display_user_balance()

nathan = User('Nathan')

nathan.account.deposit(100)
nathan.display_user_balance()