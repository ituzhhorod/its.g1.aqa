import pytest
from wallet import Wallet, InsufficientAmount


def test_default_initial_amount():
   wallet = Wallet()
   assert wallet.balance == 0


def test_set_initial_amount():
   wallet = Wallet(10)
   assert wallet.balance == 10


def test_amount_adding():
   wallet = Wallet(10)
   wallet.add_cash(20)
   assert wallet.balance == 30


def test_amount_spending():
   wallet = Wallet(50)
   wallet.spend_cash(30)
   assert wallet.balance == 20


def test_insufficient_amount():
   wallet = Wallet(50)
   with pytest.raises(InsufficientAmount):
       wallet.spend_cash(300)


