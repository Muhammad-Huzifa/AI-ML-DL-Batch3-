class Account:
    def __init__(self, card, pin, name, acc_type, balance):
        self.__card = card
        self.__pin = pin
        self.__name = name
        self.__type = acc_type
        self.__balance = balance
        self.__transactions = []

    def verify_pin(self, pass_pin):
        return self.__pin == pass_pin

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        self.__transactions.append(f"Deposited {amount}")

    def withdraw(self, amount):
        raise NotImplementedError("Override this method")

    def get_transaction_history(self):
        return self.__transactions

    def get_card(self):
        return self.__card

    def get_name(self):
        return self.__name
    def get_acc_type(self):
        return self.__type
    # helper methods
    def _deduct(self, amount):
        self.__balance -= amount

    def _add_transaction(self, msg):
        self.__transactions.append(msg)


# -------------------------
# Savings Account
# -------------------------
class SavingsAccount(Account):
    def __init__(self, card, pin, name, balance, min_balance):
        super().__init__(card, pin, name, "SavingsAccount", balance)
        self.__min_balance = min_balance

    def withdraw(self, amount):
       if amount > 1000:
            print("❌ Exceeds daily limit!")
       elif amount > self.get_balance():
            print("❌ Insufficient balance!")
       elif amount < 0:
           print("Amount Should be Positive")
       else:
            self._deduct(amount)
            self._add_transaction(f"Withdrawn {amount:.2f}")


# -------------------------
# Current Account
# -------------------------
class CurrentAccount(Account):
    def __init__(self, card, pin, name, balance, overdraft):
        super().__init__(card, pin, name, "Current", balance)
        self.__overdraft = overdraft

    def withdraw(self, amount):
       if amount > 1000:
            print("❌ Exceeds daily limit!")
       elif amount > self.get_balance() + self.__overdraft:
            print("❌ Insufficient balance!")
       elif amount < 0:
           print("Amount Should be Positive")
       else:
            self._deduct(amount)
            self._add_transaction(f"Withdrawn {amount:.2f}")