# ==========================================
# Name: Fahad
# Roll Number: [Apna Roll No yahan likhein]
# Date: November 11, 2026
# Assignment: Python Mastery - Part 1
# Topic: Variables, Data Types, Input & Output
# ==========================================

print("       PART 1: WARM-UP (Student ID Card)  ")


name = input("Enter your name: ")
age_str = input("Enter your age: ")
student_class = input("Enter your class: ")
city = input("Enter your city: ")

age = int(age_str)

print("\n======== STUDENT CARD ========")
print(f"Name : {name}")
print(f"Age  : {age}")
print(f"Class: {student_class}")
print(f"City : {city}")
print("==============================")

# type() use for checking the data types of variables
print("\n--- Data Types Check ---")
print(f"Type of name: {type(name)}")
print(f"Type of age: {type(age)}")
print(f"Type of student_class: {type(student_class)}")
print(f"Type of city: {type(city)}")



print("       PART 1: BUILD (Shop Bill)          ")


# Item ki details input lena
item_name = input("Enter item name: ")
# Price decimal (float) ho sakti hai jaise 150.50
price = float(input("Enter price per item: "))
# Quantity whole number (int) hoti hai jaise 2 ya 3
quantity = int(input("Enter quantity: "))

# Calculations
subtotal = price * quantity
discount = subtotal * 0.05               # 5% Discount
discounted_amount = subtotal - discount  # Discount ke baad amount
tax = discounted_amount * 0.17           # 17% Tax on discounted amount
final_total = discounted_amount + tax    # Aakhri total bill

# Results ko 2 decimal places (.2f) ke sath print karna
print("\n------------- RECEIPT -------------")
print(f"Item: {item_name}")
print(f"Subtotal:          Rs {subtotal:.2f}")
print(f"Discount (5%):     Rs {discount:.2f}")
print(f"Tax (17%):         Rs {tax:.2f}")
print(f"Final Total:       Rs {final_total:.2f}")
print("-----------------------------------")



print("     PART 1: CHALLENGE (Unit Converter)   ")


celsius = float(input("Enter temperature in Celsius: "))
km = float(input("Enter distance in kilometres: "))

# Conversions
# Formula: F = (C * 9/5) + 32
fahrenheit = (celsius * 9 / 5) + 32
# Formula: K = C + 273.15
kelvin = celsius + 273.15

# Distance conversions
# 1 km = 0.621371 miles
miles = km * 0.621371
# 1 km = 1000 metres
metres = km * 1000.0

# 1 decimal place (.1f) ke sath print karna
print("\n--- Temperature Conversion ---")
print(f"{celsius:.1f} C = {fahrenheit:.1f} F")
print(f"{celsius:.1f} C = {kelvin:.1f} K")

print("\n--- Distance Conversion ---")
print(f"{km:.1f} km = {miles:.1f} miles")
print(f"{km:.1f} km = {metres:.1f} metres")
