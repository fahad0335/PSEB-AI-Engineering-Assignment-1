# ==========================================
# Name: Shah Fahad
# Roll Number: TRN-2026-000706
# Date: November 11, 2026
# Assignment: Python Mastery - Part 6
# Topic: References and Mutability
# ==========================================

import copy

print("     PART 6: WARM-UP (Predict, Then Run)  ")

# Code from assignment:
a = [1, 2, 3]

# Prediction 1:
# 'b = a' does not create a new list; it creates a new reference to the same list.
# Modifying 'b' will also modify 'a'.
# Predicted output: [1, 2, 3, 4]
b = a
b.append(4)
print("a after modifying b:", a)  # Result: [1, 2, 3, 4]

# Prediction 2:
# 'c = a.copy()' creates a new independent copy of the list.
# Modifying 'c' will NOT affect 'a'.
# Predicted output: a is [1, 2, 3, 4], c is [1, 2, 3, 4, 5]
c = a.copy()
c.append(5)
print("a and c:", a, c)  # Result: [1, 2, 3, 4] [1, 2, 3, 4, 5]

# Identity ('is') vs Equality ('=='):
# 'a is b' -> True (both point to the exact same memory location)
# 'a is c' -> False (c is a separate object in memory)
# 'a == a[:]' -> True (values inside the lists are identical)
print("Identity checks (a is b, a is c, a == a[:]):")
print(a is b, a is c, a == a[:])



print("\n       PART 6: BUILD (Fix the Cart Bug)   ")


# Buggy function: Using a mutable default argument cart=[]
# In Python, default arguments are created once when the function is defined,
# not every time the function is called.
def add_item_buggy(item, cart=[]):
    cart.append(item)
    return cart

print("--- Demonstrating the Bug ---")
# Customer 1 adds apple:
cart1 = add_item_buggy("apple")
print("Customer 1 cart:", cart1)

# Customer 2 adds banana, expecting a fresh new cart:
# BUG: Customer 2 sees Customer 1's apple!
cart2 = add_item_buggy("banana")
print("Customer 2 cart (Shared Bug):", cart2)


# Fixed function: Use None as default and create a fresh list inside
def add_item_fixed(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

print("\n--- Demonstrating the Fix using None ---")
fixed_cart1 = add_item_fixed("apple")
print("Customer 1 cart (Fixed):", fixed_cart1)

fixed_cart2 = add_item_fixed("banana")
print("Customer 2 cart (Fixed):", fixed_cart2)



print("\n     PART 6: CHALLENGE (Safe Class Copy)  ")


# Original dictionary with a nested list
classes = {"A": ["Ali", "Sara"]}

# 1. Shallow copy: Only copies outer dictionary; inner list is still shared!
shallow_classes = copy.copy(classes)

# 2. Deep copy: Recursively copies outer dictionary AND all nested lists/objects!
deep_classes = copy.deepcopy(classes)

# Adding student "Zain" via shallow copy
shallow_classes["A"].append("Zain")

# Adding student "Hamza" via deep copy
deep_classes["A"].append("Hamza")

print("--- Comparing Original, Shallow, and Deep Copies ---")
print("Original classes: ", classes)
print("Shallow copy:     ", shallow_classes)
print("Deep copy:        ", deep_classes)

print("\nExplanation:")
print("- In shallow copy, modifying nested list 'A' affected the original 'classes'.")
print("- In deep copy, modifying nested list 'A' remained completely isolated.")
