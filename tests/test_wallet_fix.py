import pytest
from wallet import Wallet, InsufficientAmount


@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()


@pytest.fixture
def wallet():
    '''Returns a Wallet instance with a balance of 20'''
    return Wallet(10)


def test_default_initial_amount(empty_wallet):
   assert empty_wallet.balance == 0


def test_amount_adding(wallet):
   wallet.add_cash(20)
   assert wallet.balance == 30


@pytest.mark.parametrize("earned,spent,expected", [
    (3, 1, 2),
    (200000, 20000, 180000)
])
def test_transactions(empty_wallet, earned, spent, expected):
    empty_wallet.add_cash(earned)
    empty_wallet.spend_cash(spent)
    assert empty_wallet.balance == expected

