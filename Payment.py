from abc import ABC, abstractmethod

# ABSTRACT CLASS
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# SUBCLASS: CreditCardPayment
class CreditCardPayment(Payment):
    def __init__(self, card_number):
        self.card_number = card_number
    
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount} for card {self.card_number}.")

# SUBCLASS: MobileMoneyPayment
class MobileMoneyPayment(Payment):
    def __init__(self, mobile_number):
        self.mobile_number = mobile_number

    def process_payment(self, amount):
        print(f"Processing mobile money payment of ${amount} for number {self.mobile_number}.")


# SUBCLASS: BankTransferPayment
class BankTransferPayment(Payment):
    def __init__(self, account_number):
        self.account_number = account_number
    
    def process_payment(self, amount):
        print(f"Processing bank transfer of ${amount} to account {self.account_number}.")


# Create payment objects in a list
payments = [
    CreditCardPayment("1234-5678-9012-3456"),
    MobileMoneyPayment("0241234567"),
    BankTransferPayment("0012345678")
]   

# Process payments using a for loop
for payment in payments:
    payment.process_payment(100)