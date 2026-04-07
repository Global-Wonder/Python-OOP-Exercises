class BankAccount:
    def __init__(self, account_number: str, account_holder_name: str, balance: float = 0.0):
        # Private attributes(encapsulation)
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__balance = balance

    # Public method: Deposit money
    def deposit(self, amount: float):
        if amount <= 0:
            print("Error: Deposit amount must be positive. ")
        else:
            self.__balance += amount
            print(f"Deposit successful. New balance: {self.__balance}")

    # Public method: Withdraw money
    def withdraw(self, amount: float):
        if amount <= 0:
            print("Error: Withdrawal amount must be positive. ")
        elif amount > self.__balance:
            print("Error: Insufficient funds. ")
        else: 
            self.__balance -= amount
            print(f"Withdrawal successful. New balance: {self.__balance}")

    # Public method: Get balance
    def get_balance(self):
        return self.__balance
    
    # Public method: Get account number
    def get_account_number(self):
        return self.__account_number
    
# Create account
if __name__ == "__main__":
    account = BankAccount("123456789", "Emmanuel Weyttey", 100.0)

    print("\n--- Initial Balance ---")
    print(account.get_balance())

    # Valid deposit
    print("\n--- Valid Deposit ---")
    account.deposit(50)

    # Invalid Deposit
    print("\n--- Invalid Deposit ---")
    account.deposit(-20)

    # Valid withdrawal
    print("\n--- Valid Withdrawal ---")
    account.withdraw(30)

    # Invalid Withdrawal( insufficient funds)
    print("\n--- Invalid Withdrawal")
    account.withdraw(500)