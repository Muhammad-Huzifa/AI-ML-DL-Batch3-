import json
import getpass
from account import SavingsAccount, CurrentAccount

class ATM:
    def __init__(self):
        self.accounts = {}
        self.current_user = None
        self.file = "data.json"
        self.load()
        
    def load(self):
        try:
            with open(self.file, "r") as f:
                data = json.load(f)

            for card, info in data.items():
                if info["type"] == "SavingsAccount":
                    acc = SavingsAccount(card, info["pin"], info["name"],
                                         info["balance"], info["min_balance"])
                else:
                    acc = CurrentAccount(card, info["pin"], info["name"],
                                         info["balance"], info["overdraft"])

                self.accounts[card] = acc
        except:
            print("Error loading file")
            

    def save(self):
        data = {}

        for card, acc in self.accounts.items():

        # check account type
            acc_type = type(acc).__name__

            if acc_type == "SavingsAccount":
                data[card] = {
                "name": acc.get_name(),
                "pin": acc._Account__pin,   # simple student way
                "type": "SavingsAccount",
                "balance": acc.get_balance(),
                "min_balance": acc._SavingsAccount__min_balance
            }

            else:  # CurrentAccount
                data[card] = {
                "name": acc.get_name(),
                "pin": acc._Account__pin,
                "type": "Current",
                "balance": acc.get_balance(),
                "overdraft": acc._CurrentAccount__overdraft
            }

        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)
        print("Data saved successfully!")

    def authenticate(self):
        print("Please Insert Card\n")

        card = input("Enter card Number: ")

        if card not in self.accounts:
            print("❌ Card not found!")
            return

        acc = self.accounts[card]
        attempts = 0

        while attempts < 3:
            pin = getpass.getpass("Enter PIN: ")
            if acc.verify_pin(pin):
                self.current_user = acc
                print("✅ Authentication successful!")
                print(f"Welcome, {acc.get_name()} ({acc.get_acc_type()})")
                return  # stop loop on successful login
            else:
                attempts += 1
                print(f"❌ Wrong PIN! Attempt {attempts} of 3")
        
        # If loop completes without return, block account
        print("🚫 PIN entered incorrectly 3 times. Account blocked!")
            

    def show_menu(self):
        while True:
            print("=" * 30 + "\n" + " " * 10 + "MAIN MENU\n" + "=" * 30)
            print("\n[ 1 ] Balance\n[ 2 ] Deposit\n[ 3 ] Withdraw\n[ 4 ] History\n[ 5 ] Exit")
            print("-" *30)
            ch = input("Choose: ")

            if ch == "1":
                print("Balance:", self.current_user.get_balance())

            elif ch == "2":
                amt = float(input("Amount: "))
                amt = round(amt, 2)
                self.current_user.deposit(amt)

            elif ch == "3":
                amt = float(input("Amount: "))
                amt = round(amt, 2)
                self.current_user.withdraw(amt)

            elif ch == "4":
                for t in self.current_user.get_transaction_history():
                    print(t)

            elif ch == "5":
                self.save()
                break
            else:
                print("❌Invalid Choice please select from 1-5 Options")
                continue