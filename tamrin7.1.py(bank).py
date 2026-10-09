#Calculator.py

def deposite(balance, amount):
    return balance + amount



#Main.py
from ..bank.account import show_balance
from ..bank.fees import apply_fee
from .calculator import deposite


balance = 1000

print(show_balance(balance))

balance = deposite(balance, 500)

print(show_balance(balance))

balance = apply_fee(balance, 50)

print(show_balance(balance))

#Account. Py
def show_balance(balance):
    return balance * 100
#Fees .py
def apply_fee(balance, fee):
    return balance - fee










