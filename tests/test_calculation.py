# import pytest
# from app.calculation import add, BankAccount, InsufficientFunds

# # Fixture para criar uma conta bancária com saldo 0
# @pytest.fixture
# def zero_bank_account():
#     return BankAccount()

# # Fixture para criar uma conta bancária com saldo 50
# @pytest.fixture
# def bank_account():
#     return BankAccount(50)

# @pytest.mark.parametrize("a, b, expected", [
#     (2, 3, 5),
#     (0, 0, 0),
#     (-1, 1, 0),
# ])
# def test_add(a, b, expected):
#     assert add(a, b) == expected

# def test_bank_set_initial_amount(bank_account):
#     assert bank_account.balance == 50

# def test_bank_default_amount(zero_bank_account):
#     assert zero_bank_account.balance == 0

# def test_withdraw(bank_account):
#     bank_account.withdraw(20)
#     assert bank_account.balance == 30

# def test_deposit(bank_account):
#     bank_account.deposit(30)
#     assert bank_account.balance == 80

# def test_collect_interest(bank_account):
#     bank_account.collect_interest()
#     assert round(bank_account.balance, 6) == 55  # Supondo que o juros seja de 10%

# @pytest.mark.parametrize("deposited, withdraw, expected", [
#     (200, 100, 100),
#     (50, 10, 40),
#     (1200, 100, 1100),
# ])
# def test_bank_transaction(zero_bank_account, deposited, withdraw, expected):
#     zero_bank_account.deposit(deposited)
#     zero_bank_account.withdraw(withdraw)
#     assert zero_bank_account.balance == expected

# def test_insufficient_funds(bank_account):
#     with pytest.raises(InsufficientFunds):  
#         bank_account.withdraw(200)
