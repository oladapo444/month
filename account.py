from insufficientFunds import InsufficientFundsException
from invalidAmountException import InvalidAmountException
from invalidPinException import InvalidPinException


class Account:
    def __init__(self, name: str, account_number: int, pin: str):
        self.__balance = 0
        self.name = name
        self.account_number = account_number
        self.pin = pin

    def deposit(self, amount: int):
        if amount <= 0:
            raise InvalidAmountException("Invalid amount")

        self.__balance += amount

    def withdraw(self, amount: int, pin: str):
        if self.pin != pin:
            raise InvalidPinException("Invalid pin")
        if amount > self.__balance:
            raise InsufficientFundsException("Amount cannot be greater than balance")
        self.__balance -= amount

    def check_balance(self, pin: str):
        if self.pin != pin:
            raise InvalidPinException("Invalid pin")
        return self.__balance
