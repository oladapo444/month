from account import Account


class Bank:
    def __init__(self, name):
        self.name = name
        self.__accounts = []

    def deposit(self, account_number: int, amount: int):
        account = self.find_account(account_number)
        account.deposit(3000)

    def withdraw(self, account_number: int, amount: int):
        account = self.find_account(account_number)
        if account.withdraw(amount):
            self.__accounts.remove(amount)

    def register_account(self, last_name, first_name, pin):
        name = last_name + ", " + first_name
        account_number = self.generate_number()
        account = Account(name, account_number, pin)
        self.__accounts.append(account)
        return account

    def find_account(self, account_number):
        for account in self.__accounts:
            if account.account_number == account_number:
                return account

    def check_balance(self, account_number, pin):
        for account in self.__accounts:
            if account.account_number == account_number:
                return account.check_balance()


    def transfer_money(self, receiver_account_number, sender_account_number, amount, pin):
        sender_account_number = self.bank.find_account(sender_account_number)
        receiver_account_number = self.bank.find_account(receiver_account_number)
        if sender_account_number is None:
            return "Account not found"
        if receiver_account_number is None:
            return "Account not found"

    @staticmethod
    def generate_number():
        account_number = 1
        account_number += 1
        return account_number

    def get_number_of_account(self):
        return len(self.__accounts)
