class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = BankAccount(account_name='', int_rate=0.02, balance=0)
    
    def make_deposit(self, amount, account_name):
        # self.account_balance += amount
        self.account_balance.deposit(amount, account_name)
        return self
    
    def make_withdrawal(self, amount, account_name):
        # self.account_balance -= amount
        self.account_balance.withdraw(amount, account_name)
        return self
    
    def display_user_balance(self):
        # print(f"User: {self.name}, Balance: {self.account_balance}")
        print(f'User: {self.name}')
        self.account_balance.display_account_info()
        return self


class BankAccount:
    def __init__(self, account_name, int_rate=0.04, balance=0):
        self.account_name = account_name
        self.int_rate = int_rate
        self.account_balance = balance
    
    def deposit(self, amount, account_name):
        self.account_balance += amount
        return self
    
    def withdraw(self, amount, account_name):
        if amount > self.account_balance:
            print('Insufficient Funds: Charging a $5 fee')
            self.account_balance = self.account_balance - 5
        else:
            self.account_balance -= amount
        return self
    
    def display_account_info(self):
        print(f'Balance:{self.account_balance}')
        return self
    
    def yield_interest(self):
        self.account_balance *= (1+self.int_rate)
        return self


Kirby = User('Kirby', 'kirbyf@yahoo.com')
Javier = User('Javier', 'javi@yahoo.com')

checking = BankAccount('Checking')
saving = BankAccount('Saving')

Kirby.make_deposit(500,checking).make_deposit(1000,checking).make_withdrawal(300,checking).account_balance.yield_interest()
Kirby.display_user_balance()
Javier.make_deposit(300,checking).make_deposit(150,saving).make_deposit(200,saving).make_withdrawal(50,checking).account_balance.yield_interest()
Javier.display_user_balance()
