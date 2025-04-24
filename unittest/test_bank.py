import pytest

from ..src.classes import Bank, BankAccount

@pytest.fixture
def bank():
    return Bank()

@pytest.fixture
def bank_with_account(bank):
    account = bank.create_account("joHn", 100)
    return bank, account

def test_bank_create_account(bank):
    j = bank.create_account("joHn", 100)
    assert str(j) == "JOHN has 100.0 dollars"

def test_bank_create_account_already_exists(bank_with_account):
    bank, _ = bank_with_account
    with pytest.raises(ValueError) as e:
        bank.create_account("joHn", 100)
    assert str(e.value) == "Account already exists"

def test_bank_get_account(bank_with_account):
    bank, _ = bank_with_account
    b = bank.get_account("joHn")
    assert str(b) == "JOHN has 100.0 dollars"
