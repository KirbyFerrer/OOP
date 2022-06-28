# class User:
# # class attributes get defined in the class 
#     bank_name = "First National Dojo"
# # now our method has 2 parameters!
#     def __init__(self, name, email_address):
#         # we assign them accordingly
#         self.name = name
#         self.email = email_address
#         # the account balance is set to $0
#         self.account_balance = 0
    
#     def make_deposit(self, amount):
#         self.account_balance += amount
    
#     def make_withdrawal(self, amount):
#         self.account_balance -= amount
#         return self
    
#     def display_user_balance(self):
#         print(f"User: {self.name}, Balance: {self.account_balance}")
#         return self

import re


class BankAccount:
    def __init__(self, account_name, int_rate=0.01, balance=0):
        self.account_name = account_name
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient Funds: Charging a $5 fee')
            self.balance = self.balance - 5
        else:
            self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f'Balance:{self.balance}')
        return self
    
    def yield_interest(self):
        self.balance *= (1+self.int_rate)
        return self

kirby = BankAccount('saving')
steve = BankAccount('checking')

kirby.deposit(500).deposit(500).deposit(500).withdraw(300).yield_interest().display_account_info()
steve.deposit(600).deposit(600).withdraw(100).withdraw(100).withdraw(50).withdraw(15).yield_interest().display_account_info()
