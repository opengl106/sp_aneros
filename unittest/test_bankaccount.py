import pytest

from ..src.classes import Bank, BankAccount

@pytest.fixture
def bank():
    return Bank()

@pytest.fixture
def accounts(bank):
    j = bank.create_account("joHn", 100)
    t = bank.create_account("tiM", 200)
    return j, t

def test_balance(accounts):
    j, t = accounts
    assert j.balance == 100.0
    assert t.balance == 200.0

def test_str(accounts):
    j, t = accounts
    assert str(j) == "JOHN has 100.0 dollars"
    assert str(t) == "TIM has 200.0 dollars"

def test_deposit(accounts):
    j, t = accounts
    j.deposit(100)
    assert j.balance == 200.0
    with pytest.raises(ValueError):
        j.deposit(-100)

def test_withdraw(accounts):
    j, t = accounts
    j.withdraw(100)
    assert j.balance == 0.0
    with pytest.raises(ValueError):
        j.withdraw(-100)
    with pytest.raises(ValueError):
        j.withdraw(1000)

def test_transfer(accounts):
    j, t = accounts
    j.transfer(t, 50)
    j.transfer("tiM", 50)
    assert j.balance == 0.0
    assert t.balance == 300.0
    with pytest.raises(ValueError):
        j.transfer(t, -1)
    with pytest.raises(ValueError):
        j.transfer("tiM", 1)
