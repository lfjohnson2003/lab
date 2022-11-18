import pytest
from _pytest.python_api import approx

from account import *


class Test:
    def setup_method(self):
        self.account_one = Account('John')


    def teardown_method(self):
        del self.account_one


    def test_init(self):
        assert self.account_one.get_name() == 'John'
        assert self.account_one.get_balance() == 0


    def test_deposit(self):
        assert self.account_one.deposit(-1) is False
        assert self.account_one.deposit(0) is False
        assert self.account_one.deposit(2) is True
        assert self.account_one.get_balance() == approx(2, abs=0.001)


    def test_withdraw(self):
        assert self.account_one.withdraw(-1) is False
        assert self.account_one.get_balance() == 0
        assert self.account_one.withdraw(0) is False
        self.account_one.deposit(2)
        assert self.account_one.get_balance() == approx(2, abs=0.001)
        assert self.account_one.withdraw(2) is True
        assert self.account_one.withdraw(20000000) is False