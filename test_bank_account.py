# ==========================================
# Name: Shah Fahad
# Roll Number: TRN-2026-000706
# Date: November 11, 2026
# Assignment: Python Mastery - Part 12 (Challenge)
# Topic: Pytest Fixtures & Error Testing
# ==========================================

import pytest

class BankAccount:
    """BankAccount class from Part 9."""
    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner
        self.balance = initial_balance
        self.history: list[str] = [f"Account opened with initial balance: Rs {initial_balance:.2f}"]

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError(f"Deposit amount must be positive. Received: {amount}")
        self.balance += amount
        self.history.append(f"Deposited: Rs {amount:.2f} | New Balance: Rs {self.balance:.2f}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError(f"Withdraw amount must be positive. Received: {amount}")
        if amount > self.balance:
            raise ValueError(f"Insufficient funds! Current balance: Rs {self.balance:.2f}, Requested: Rs {amount:.2f}")
        self.balance -= amount
        self.history.append(f"Withdrew: Rs {amount:.2f} | New Balance: Rs {self.balance:.2f}")


# Fixture that returns an account initialized with Rs 1000
@pytest.fixture
def account_with_1000():
    return BankAccount(owner="Shah Fahad", initial_balance=1000.0)


def test_deposit(account_with_1000):
    """Test valid deposit increases balance."""
    account_with_1000.deposit(500.0)
    assert account_with_1000.balance == 1500.0


def test_withdraw(account_with_1000):
    """Test valid withdraw decreases balance."""
    account_with_1000.withdraw(300.0)
    assert account_with_1000.balance == 700.0


def test_transaction_history(account_with_1000):
    """Test that transaction history records all operations."""
    account_with_1000.deposit(200.0)
    account_with_1000.withdraw(100.0)
    assert len(account_with_1000.history) == 3
    assert "Deposited: Rs 200.00" in account_with_1000.history[1]
    assert "Withdrew: Rs 100.00" in account_with_1000.history[2]


def test_negative_deposit_error(account_with_1000):
    """Test deposit refuses negative amount with ValueError."""
    with pytest.raises(ValueError):
        account_with_1000.deposit(-50.0)


def test_insufficient_funds_error(account_with_1000):
    """Test withdraw refuses amount exceeding balance with ValueError."""
    with pytest.raises(ValueError):
        account_with_1000.withdraw(5000.0)
