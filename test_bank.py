import account
from account import Account
from bank import Bank

import unittest

class TestBank(unittest.TestCase):

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.__accounts = 1

    def setUp(self):
        self.bank = Bank("gidx")
        self.account = self.bank.register_account("lastname", "firstname", "pin")
    def test_account_creation(self):
        self.bank_account = self.bank.register_account("Oladapo", "Olamide", "1111")
        self.bank_account = self.bank.register_account("Otusaya", "emmanuel", "5555")
        self.bank_account = self.bank.register_account("ore", "reve", "4444")

    def test_can_find_account(self):
        self.bank.generate_number()
        self.assertEqual("1")
        self.bank.register_account("Oladapo", "Olamide", "1111")

     def test_for_deposit(self, account_number):
            self.bank.generate_number()
            self.bank.deposit(account_number, 3000)
            self.assertEqual(self.bank_account.__get_balance())

    def test_for_withdrawal(self, account_number):
            self.bank.generate_number()
            self.bank.withdraw("1111",1000)
            self.assertEqual(self.bank_account.__get_balance())

    def test_transfer(self,  receiver_account_number, sender_account_number):
            self.bank.generate_number()
            self.bank.transfer_money(receiver_account_number,sender_account_number,1000,"1111")
            self.assertEqual(self.bank_account.__get_balance())

    def check_balance(self):
            self.bank.generate_number()
            self.bank.check_balance("1111")
            self.assertEqual(self.bank_account)

    def test_to_find_account(self, account_number) :
            self.bank.generate_number()
            self.bank_account = self.bank.register_account("Oladapo", "Olamide", "1111")
            self.assertEqual(1, self.bank.find_account)