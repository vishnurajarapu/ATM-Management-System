# Import ABC Abstract Class
from abc import ABC, abstractmethod
#ABSTRACTION
class BankAccount(ABC):     # ABSTRACT CLASS
    @abstractmethod
    def transaction(self):
        pass   # do nothing


# ENCAPSULATION
class Account(BankAccount):     # account base class

    # Constructor
    def __init__(self, name, acc_no, balance):    # initialize data

        self.name = name    # Public variable

        self._acc_no = acc_no   # Protected variable

        self.__balance = balance    # Private variable

    def get_balance(self):    # get private balance
        return self.__balance

    def set_balance(self, amount):    # update private balance
        self.__balance = amount

    # Polymorphism
    def transaction(self):
        print("Bank transaction is processing...")

# INHERITANCE
class ATM(Account):

    # Class variable
    bank_name = "ABC BANK"

    # Overriding abstract method
    def transaction(self):
        print("ATM transaction started successfully.")

    @classmethod
    def display_bank_name(cls):
        print("WELCOME TO", cls.bank_name, "ATM")
    # STATIC METHOD

    @staticmethod
    def validate_amount(amount):
        if amount > 0:
            return True
        else:
            return False

    # INSTANCE METHODS

    def check_balance(self):
        print("Your current balance is:", self.get_balance())

    def deposit(self, amount):
        if ATM.validate_amount(amount):
            new_balance = self.get_balance() + amount
            self.set_balance(new_balance)
            print("Deposit successful.")
            print("Updated balance:", self.get_balance())
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if not ATM.validate_amount(amount):
            print("Invalid withdrawal amount.")
            return

        if amount <= self.get_balance():
            new_balance = self.get_balance() - amount
            self.set_balance(new_balance)
            print("Withdrawal successful.")
            print("Remaining balance:", self.get_balance())
        else:
            print("Insufficient balance.")

    def account_details(self):
        print("--------------------------------")
        print("Account Holder Name :", self.name)
        print("Account Number      :", self._acc_no)
        print("Account Balance     :", self.get_balance())
        print("--------------------------------")
# Create ATM object
user = ATM("eswar", 12345, 1000)

# Display bank name
ATM.display_bank_name()

print("--------------------------------")
print("Account Holder Name :", user.name)     #DISPLAY AC HOLDER NAME
print("Account Number      :", user._acc_no)  #DISPLAY AC NUMBER
print("--------------------------------")

# Infinite loop
while True:

    print("\nATM MENU")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Account Details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        user.check_balance()

    elif choice == "2":
        amount = int(input("Enter amount to deposit: "))
        user.deposit(amount)

    elif choice == "3":
        amount = int(input("Enter amount to withdraw: "))
        user.withdraw(amount)

    elif choice == "4":
        user.account_details()

    elif choice == "5":
        print("Thank you for using ABC bank ATM.")
        break   # Exit the loop

    else:
        print("Invalid choice! Please try again.")
