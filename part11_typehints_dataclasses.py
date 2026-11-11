# ==========================================
# Name: Shah Fahad
# Roll Number: TRN-2026-000706
# Date: November 11, 2026
# Assignment: Python Mastery - Part 11
# Topic: Type Hints and Dataclasses
# ==========================================

from dataclasses import dataclass, field, asdict
import json
import math

print("==========================================")
print("       PART 11: WARM-UP (Type Hints)      ")
print("==========================================")

# Part 5 functions annotated with strict type hints and return types
def area_of_circle(r: float) -> float:
    """Calculate area of circle given radius r."""
    return math.pi * (r ** 2)

def is_even(n: int) -> bool:
    """Return True if n is even, False otherwise."""
    return n % 2 == 0

def greet(name: str, lang: str = "en") -> str:
    """Greet user in English or Urdu."""
    if lang == "ur":
        return f"Salaam, {name}!"
    return f"Hello, {name}!"

def average(marks: list[float]) -> float:
    """Calculate average of float marks."""
    if not marks:
        return 0.0
    return sum(marks) / len(marks)

def grade(avg: float) -> str:
    """Return letter grade from average marks."""
    if avg < 0 or avg > 100:
        return "Invalid"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 33:
        return "D"
    return "Fail"

print("Type-hinted helper functions loaded successfully.")
print(f"Sample call - greet: {greet('Fahad', lang='ur')}")
print(f"Sample call - average: {average([80.0, 90.0, 85.0]):.2f}")


print("\n==========================================")
print("     PART 11: BUILD (Product Dataclass)   ")
print("==========================================")

@dataclass(order=True)
class Product:
    # sort_index ensures sorting by price when order=True
    sort_index: float = field(init=False, repr=False)
    name: str = field(compare=False)
    price: float = field(compare=True)
    stock: int = field(compare=False)
    tags: list[str] = field(default_factory=list, compare=False)

    def __post_init__(self):
        """Validate that price and stock are not negative."""
        if self.price < 0:
            raise ValueError(f"Price cannot be negative: {self.price}")
        if self.stock < 0:
            raise ValueError(f"Stock cannot be negative: {self.stock}")
        # Set sort_index to price for automatic price sorting
        self.sort_index = self.price

# Store 5 sample products
catalog = [
    Product(name="Wireless Mouse", price=1500.0, stock=10, tags=["electronics", "pc"]),
    Product(name="Mechanical Keyboard", price=4500.0, stock=0, tags=["electronics", "gaming"]),
    Product(name="USB-C Cable", price=500.0, stock=25, tags=["accessories"]),
    Product(name="Gaming Headset", price=3200.0, stock=0, tags=["audio", "gaming"]),
    Product(name="Laptop Stand", price=1800.0, stock=5, tags=["ergonomics"])
]

print("--- Out of Stock Products (Stock == 0) ---")
for p in catalog:
    if p.stock == 0:
        print(f"  [OUT OF STOCK] {p.name} - Price: Rs {p.price:.2f}")


print("\n==========================================")
print("    PART 11: CHALLENGE (Save and Load)    ")
print("==========================================")

JSON_FILE = "products.json"

# 1. Save products list to products.json using asdict
# Note: we exclude internal sort_index by passing standard dicts
serialized_products = []
for p in catalog:
    prod_dict = asdict(p)
    prod_dict.pop("sort_index", None)  # exclude internal sort field
    serialized_products.append(prod_dict)

with open(JSON_FILE, "w", encoding="utf-8") as f:
    json.dump(serialized_products, f, indent=4)

print(f"Products successfully saved to '{JSON_FILE}'.")

# 2. Load products back into Product objects using Product(**d)
with open(JSON_FILE, "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

loaded_products: list[Product] = [Product(**item) for item in loaded_data]
print(f"Loaded {len(loaded_products)} Product objects from JSON.")

# 3. Sort products by price (order=True uses price as primary comparison)
loaded_products.sort()

print("\n--- Products Sorted by Price (Lowest to Highest) ---")
for p in loaded_products:
    print(f"  Rs {p.price:>7.2f} | {p.name:<22} | Stock: {p.stock:<2} | Tags: {p.tags}")
