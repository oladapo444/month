import unittest

from account import Account
from insufficientFunds import InsufficientFundsException
from invalidAmountException import InvalidAmountException
from invalidPinException import InvalidPinException


class accountTest(unittest.TestCase):

    def setUp(self):
        self.account = Account("emmanuel", 1234567, "1111")

    def test_account_deposit(self):
        self.assertEqual(self.account.check_balance("1111"), 0)

        self.account.deposit(900)
        self.assertEqual(self.account.check_balance("1111"), 900)

    def test_account_withdraw(self):
        self.account.deposit(900)
        self.assertEqual(self.account.check_balance("1111"), 900)
        self.account.withdraw(700, "1111")
        self.assertEqual(self.account.check_balance("1111"), 200)

    def test_check_balance_with_wrong_pin_throws_Exception(self):
        self.account.deposit(200)
        with self.assertRaises(InvalidPinException):
            self.account.check_balance("2323")

    def test_deposit_invalid_amount_throws_Exception(self):
        with self.assertRaises(InvalidAmountException):
            self.account.deposit(-500)
            self.assertEqual(self.account.check_balance("1111"), 0)

    def test_withdraw_amount_greater_than_balance_throws_Exception(self):
        with self.assertRaises(InsufficientFundsException):
            self.account.withdraw(10000, "1111")
            self.assertEqual(self.account.check_balance("1111"), 0)

