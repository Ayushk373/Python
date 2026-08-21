import random

class BankAccount:
    def __init__(self, name, initial_deposit):
        self.name = name
        self.account_number = random.randint(10000, 99999)
        self.balance = initial_deposit
        print(f"\n Account created successfully!")
        print(f"Holder: {self.name} | Account Number: {self.account_number}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\n Deposited ${amount:.2f}. New Balance: ${self.balance:.2f}")
        else:
            print("\n Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount <= 0:
            print("\n Withdrawal amount must be positive!")
        elif amount > self.balance:
            print(f"\n Insufficient funds! Current Balance: ${self.balance:.2f}")
        else:
            self.balance -= amount
            print(f"\n Withdrew ${amount:.2f}. Remaining Balance: ${self.balance:.2f}")

    def display_balance(self):
        print(f"\n Current Balance for Account {self.account_number}: ${self.balance:.2f}")


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        name = input("Enter account holder's name: ").strip()
        if not name:
            print("\n Name cannot be empty!")
            return

        try:
            initial_deposit = float(input("Enter initial deposit amount: $"))
            if initial_deposit < 0:
                print("\n Initial deposit cannot be negative!")
                return
        except ValueError:
            print("\n Invalid amount! Please enter numbers only.")
            return

        new_account = BankAccount(name, initial_deposit)
        self.accounts[new_account.account_number] = new_account

    def get_account(self):
        try:
            acc_num = int(input("Enter 5-digit account number: "))
            if acc_num in self.accounts:
                return self.accounts[acc_num]
            else:
                print("\n Account not found!")
                return None
        except ValueError:
            print("\n Invalid account number format!")
            return None

    def run(self):
        while True:
            print("\n" + "="*30)
            print("      BANKING SYSTEM MENU      ")
            print("="*30)
            print("1. Create New Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check Balance")
            print("5. Exit")
            
            choice = input("Enter your choice (1-5): ").strip()

            if choice == '1':
                self.create_account()
            elif choice == '2':
                account = self.get_account()
                if account:
                    try:
                        amount = float(input("Enter deposit amount: $"))
                        account.deposit(amount)
                    except ValueError:
                        print("\n Invalid input! Enter a valid number.")
            elif choice == '3':
                account = self.get_account()
                if account:
                    try:
                        amount = float(input("Enter withdrawal amount: $"))
                        account.withdraw(amount)
                    except ValueError:
                        print("\n Invalid input! Enter a valid number.")
            elif choice == '4':
                account = self.get_account()
                if account:
                    account.display_balance()
            elif choice == '5':
                print("\n Thank you for using our banking system. Goodbye!")
                break
            else:
                print("\n Invalid choice! Please select between 1 and 5.")


if __name__ == "__main__":
    system = BankSystem()
    system.run()
