# Introduction

A sample Python project of a bank account management system.

# Prerequisites

Run the following command to install the dependencies:

```bash
pip install -r requirements.txt
```

# Tests Coverage

Run the following command to run the tests:

```bash
pytest --cov=src unittest/
```

# Example Usage

```python
>>> from src.classes import Bank
>>> b = Bank()
>>> b.load_from_csv("unittest/fuck.csv")
>>> str(b.get_account("joHn"))
'JOHN has 47.01 dollars'
>>> str(b.get_account("tiM"))
'TIM has 23.01 dollars'
>>> m = b.create_account("Matt")
>>> m.deposit(0.0001)
>>> str(m)
'MATT has 0.0 dollars'
>>> m.deposit(0.008)
>>> str(m)
'MATT has 0.01 dollars'
>>> m.deposit(20)
>>> m.withdraw(20.011)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/mnt/d/[LABMIKAZU]/[3-SECRET]/pj_foucauldian/pj_c/sp_aneros/src/classes.py", line 25, in withdraw
    raise ValueError("Overdraft is not allowed")
ValueError: Overdraft is not allowed
>>> t = b.get_account("tim")
>>> m.transfer(t, 12.013)
>>> m.transfer("john", 2.006)
>>> str(m)
'MATT has 5.99 dollars'
>>> str(t)
'TIM has 35.02 dollars'
>>> str(b.get_account("john"))
'JOHN has 49.02 dollars'
>>>
```
