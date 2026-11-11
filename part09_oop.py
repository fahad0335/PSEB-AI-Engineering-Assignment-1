# ==========================================
# Name: Shah Fahad
# Roll Number: TRN-2026-000706
# Date: November 11, 2026
# Assignment: Python Mastery - Part 9
# Topic: OOP — Classes and Objects
# ==========================================

print("==========================================")
print("        PART 9: WARM-UP (Student Class)   ")
print("==========================================")

class Student:
    """Class representing a student with marks and roll number."""
    def __init__(self, name: str, roll_number: int):
        self.name = name
        self.roll_number = roll_number
        self.marks: list[float] = []

    def add_mark(self, mark: float) -> None:
        """Add a mark to student's marks list."""
        self.marks.append(mark)

    def average(self) -> float:
        """Calculate the average mark."""
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)

    def __str__(self) -> str:
        """String representation of student: e.g., Ali (Roll 12): avg 81.0"""
        return f"{self.name} (Roll {self.roll_number}): avg {self.average():.1f}"

# Test Student class
student1 = Student("Ali", 12)
student1.add_mark(80.0)
student1.add_mark(72.0)
student1.add_mark(91.0)
print(student1)


print("\n==========================================")
print("      PART 9: BUILD (Bank Account)        ")
print("==========================================")

class BankAccount:
    """Class representing a bank account with deposit, withdraw, and history."""
    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner
        self.balance = initial_balance
        self.history: list[str] = [f"Account opened with initial balance: Rs {initial_balance:.2f}"]

    def deposit(self, amount: float) -> None:
        """Deposit money into account. Refuses non-positive amounts."""
        if amount <= 0:
            raise ValueError(f"Deposit amount must be positive. Received: {amount}")
        self.balance += amount
        self.history.append(f"Deposited: Rs {amount:.2f} | New Balance: Rs {self.balance:.2f}")

    def withdraw(self, amount: float) -> None:
        """Withdraw money from account. Refuses invalid or excess amounts."""
        if amount <= 0:
            raise ValueError(f"Withdraw amount must be positive. Received: {amount}")
        if amount > self.balance:
            raise ValueError(f"Insufficient funds! Current balance: Rs {self.balance:.2f}, Requested: Rs {amount:.2f}")
        self.balance -= amount
        self.history.append(f"Withdrew: Rs {amount:.2f} | New Balance: Rs {self.balance:.2f}")

    def print_history(self) -> None:
        """Print full transaction history."""
        print(f"\nTransaction History for {self.owner}:")
        for transaction in self.history:
            print(f"  - {transaction}")

# Test BankAccount
acc = BankAccount("Shah Fahad", 1000.0)
acc.deposit(500.0)
acc.withdraw(200.0)

# Test error handling with invalid transactions
try:
    acc.deposit(-50.0)
except ValueError as e:
    print(f"\nCaught expected error on deposit: {e}")

try:
    acc.withdraw(5000.0)
except ValueError as e:
    print(f"Caught expected error on withdraw: {e}")

acc.print_history()


print("\n==========================================")
print("     PART 9: CHALLENGE (Library System)   ")
print("==========================================")

class Book:
    """Base Book class."""
    def __init__(self, title: str, author: str, available: bool = True):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self) -> str:
        status = "Available" if self.available else "Borrowed"
        return f"'{self.title}' by {self.author} [{status}]"

class EBook(Book):
    """EBook class inheriting from Book and adding file_size."""
    def __init__(self, title: str, author: str, file_size_mb: float, available: bool = True):
        # Call parent constructor using super()
        super().__init__(title, author, available)
        self.file_size_mb = file_size_mb

    def __str__(self) -> str:
        """Overriding __str__ to include file size."""
        status = "Available" if self.available else "Borrowed"
        return f"[E-Book] '{self.title}' by {self.author} ({self.file_size_mb} MB) [{status}]"

class Library:
    """Library demonstrating composition (holds a collection of Book objects)."""
    def __init__(self, name: str):
        self.name = name
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        """Add a Book or EBook to the library."""
        self.books.append(book)

    def borrow(self, title: str) -> bool:
        """Borrow a book by its title."""
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                print(f"Successfully borrowed: '{book.title}'")
                return True
        print(f"Cannot borrow '{title}': Not available or not found.")
        return False

    def return_book(self, title: str) -> bool:
        """Return a borrowed book by its title."""
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                print(f"Successfully returned: '{book.title}'")
                return True
        print(f"Cannot return '{title}': Was not borrowed or not found.")
        return False

    def available_books(self) -> list[Book]:
        """Return list of all currently available books."""
        return [book for book in self.books if book.available]

# Test Library System
city_library = Library("City Public Library")

# Add physical books and eBooks
b1 = Book("Python Crash Course", "Eric Matthes")
b2 = Book("Clean Code", "Robert C. Martin")
eb1 = EBook("Fluent Python", "Luciano Ramalho", file_size_mb=8.5)

city_library.add_book(b1)
city_library.add_book(b2)
city_library.add_book(eb1)

print("\n--- Available Books in Library ---")
for book in city_library.available_books():
    print(" ", book)

# Borrow a book
print("\nBorrowing 'Clean Code':")
city_library.borrow("Clean Code")

print("\n--- Available Books After Borrowing ---")
for book in city_library.available_books():
    print(" ", book)

# Return the book
print("\nReturning 'Clean Code':")
city_library.return_book("Clean Code")
