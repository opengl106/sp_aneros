import pytest
import os
import filecmp

from ..src.classes import Bank

@pytest.fixture
def bank():
    return Bank()

@pytest.fixture
def bank_with_account(bank):
    bank.create_account("joHn", 100)
    return bank

def test_bank_create_account(bank):
    j = bank.create_account("joHn", 100)
    assert str(j) == "JOHN has 100.0 dollars"

def test_bank_create_account_already_exists(bank_with_account):
    with pytest.raises(ValueError) as e:
        bank_with_account.create_account("joHn", 100)
    assert str(e.value) == "Account already exists"

def test_bank_get_account(bank_with_account):
    b = bank_with_account.get_account("joHn")
    assert str(b) == "JOHN has 100.0 dollars"

def test_bank_save_to_csv(bank_with_account):
    if os.path.exists("unittest/shit.csv"):
        os.remove("unittest/shit.csv")
    bank_with_account.save_to_csv("unittest/shit.csv")
    assert os.path.exists("unittest/shit.csv")
    assert filecmp.cmp("unittest/shit.csv", "unittest/shit_sample.csv", shallow=False)

def test_bank_load_from_csv(bank):
    bank.load_from_csv("unittest/fuck.csv")
    assert str(bank.get_account("joHn")) == "JOHN has 47.01 dollars"
    assert str(bank.get_account("tiM")) == "TIM has 23.01 dollars"
