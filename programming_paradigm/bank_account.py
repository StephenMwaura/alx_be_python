class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance
    def deposit(self,amount ):
        if amount > 0:
          self._account_balance += amount
        
    def withdraw(self,amount):
        if self._account_balance >= amount:
            self._account_balance -= amount
            return True
        else:
            return False
    def display_balance(self):
        return  f"Current Balance:{self._account_balance}"
    def __str__(self):
        return f"Bankaccount(balance={self._account_balance})"
     