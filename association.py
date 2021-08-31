class User:		# here's what we have so far
    def __init__(self, name, email): # makes the instance of the class
        self.name = name
        self.email = email
        self.account_balance = 0
        self.account = BankAccount(self.int_rate,self.balance)
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account.deposit(amount)
        return self
    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        # print(self.account_balance)
        self.account.display_account_info(self)
        return self

    def transfer(self,amount,user):
        self.account_balance -= amount
        user.account_balance += amount
        self.display_user_balance()
        user.display_user_balance()


    
guido = User('Guido', 'guido@gmail.com')
monty = User('Monty', 'monty@gmail.com')
micheal = User('Micheal', 'micheal@gmail.com')

guido.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawl(50).display_user_balance()

monty.make_deposit(200).make_deposit(200).make_withdrawl(100).make_withdrawl(100).display_user_balance()

micheal.make_deposit(500).make_withdrawl(120).make_withdrawl(120).make_withdrawl(120).display_user_balance()

guido.transfer(150, micheal)


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
        print(f'Balance: {self.balance}')
        return self
    
    @classmethod
    def print_info(cls):
        for account in cls.accounts:
            account.display_account_info()

savings = BankAccount(0.5,3000)
checking = BankAccount(0.2,900)

savings.deposit(100).deposit(100).deposit(200).withdraw(100).yield_interest().display_account_info()
checking.deposit(200).deposit(300).withdraw(50).withdraw(150).withdraw(220).withdraw(450).yield_interest().display_account_info()

BankAccount.print_info()