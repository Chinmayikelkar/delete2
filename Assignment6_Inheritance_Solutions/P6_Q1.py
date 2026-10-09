# Q1. Bank Application - Single Inheritance

class Account:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = float(balance)

    def check_balance(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Current balance: ₹{self.balance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        self.balance += amount
        print(f"₹{amount:.2f} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount:.2f} withdrawn successfully.")


class SavingAccount(Account):
    def __init__(self, account_holder, balance=0.0, interest_rate=4.0):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        print(f"Interest at {self.interest_rate:.2f}%: ₹{interest:.2f}")
        return interest


def main():
    account = SavingAccount(input("Enter account holder name: "),
                            float(input("Enter opening balance: ₹")),
                            float(input("Enter annual interest rate (%): ")))
    while True:
        print("\n1. Deposit  2. Withdraw  3. Check balance  4. Calculate interest  5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            account.deposit(float(input("Amount to deposit: ₹")))
        elif choice == "2":
            account.withdraw(float(input("Amount to withdraw: ₹")))
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            account.calculate_interest()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
