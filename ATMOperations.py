from abc import ABC, abstractmethod

# ABSTRACT CLASS
class ATMOperations:
    @abstractmethod
    def withdraw(self, amount):
        pass
    
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass


# SUBCLASS: BankATM
class BankATM(ATMOperations):
    def __init__(self, initial_balance = 0):
        # Private attribute to hide internal balance
        self.__balance = initial_balance
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")

    def check_balance(self):
        print(f"Current balance: ${self.__balance}.")


# TEST SCRIPT
if __name__ == "__main__":
    atm = BankATM(500) 

    print("=== ATM Operations Demo ===")
    atm.check_balance()
    atm.deposit(200)
    atm.withdraw(100)
    atm.withdraw(700)
    atm.check_balance()
