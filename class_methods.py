class BankAccount:
    # Class variable
    bank_name = "Tech4Girls Bank"
    
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    @staticmethod
    def bank_policy():
        print("Our bank policy is to provide the best service to our customers and ensure their satisfaction.")

    @classmethod
    def get_bank_name(cls):
        return cls.bank_name

# Demonstrate creating instances and calling methods
# Create instances
account1 = BankAccount("Habiba")
account2 = BankAccount("Irene")

# Call instance methods
account1.deposit(1000)
account1.withdraw(300)

account2.deposit(2000)
account2.withdraw(2500)

# Call static method
BankAccount.bank_policy()

# Call class method
print(BankAccount.get_bank_name())
