class User:
# class attributes get defined in the class 
    bank_name = "First National Dojo"
# now our method has 2 parameters!
    def __init__(self, name, email_address):
        # we assign them accordingly
        self.name = name
        self.email = email_address
        # the account balance is set to $0
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
kirby = User('Kirby Ferrer', 'kirbyf@yahoo.com')

guido.make_deposit(200)
guido.make_deposit(200)
guido.make_deposit(300)
guido.make_withdrawal(200)
guido.display_user_balance()
monty.make_deposit(300)
monty.make_deposit(500)
monty.make_withdrawal(100)
monty.make_withdrawal(150)
monty.display_user_balance()
kirby.make_deposit(300)
kirby.make_withdrawal(50)
kirby.make_withdrawal(100)
kirby.make_withdrawal(50)
kirby.display_user_balance()





