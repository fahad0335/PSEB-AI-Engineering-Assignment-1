# ==========================================
# Name: Shah Fahad
# Roll Number: TRN-2026-000706
# Date: November 11, 2026
# Assignment: Python Mastery - Part 2
# Topic: Conditions (if / elif / else)
# ==========================================

print("==========================================")
print("     PART 2: WARM-UP (Even, Odd & Sign)   ")
print("==========================================")

# Take an integer input from the user
num = int(input("Enter an integer number: "))

# 1. Check sign: Positive, Negative, or Zero
if num > 0:
    sign = "Positive"
elif num < 0:
    sign = "Negative"
else:
    sign = "Zero"

# 2. Check parity: Even or Odd
# The modulo operator (%) returns the remainder.
# If divided by 2 gives remainder 0, it is Even.
if num % 2 == 0:
    parity = "Even"
else:
    parity = "Odd"

print(f"Result: The number {num} is {sign} and {parity}.")


print("\n==========================================")
print("     PART 2: BUILD (Grade Calculator)     ")
print("==========================================")

marks = float(input("Enter marks out of 100: "))

# Validate input marks: must be between 0 and 100
if marks < 0 or marks > 100:
    print("Invalid marks! Marks must be between 0 and 100.")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 33:
    print("Grade: D")
else:
    print("Grade: Fail")


print("\n==========================================")
print("   PART 2: CHALLENGE (Electricity Bill)   ")
print("==========================================")

units = float(input("Enter electricity units used: "))

if units < 0:
    print("Units cannot be negative!")
else:
    # Tariff slabs:
    # 1. First 100 units = Rs 10 each
    # 2. Next 100 units (101-200) = Rs 15 each
    # 3. Units above 200 = Rs 20 each
    # Fixed charges = Rs 50
    fixed_charges = 50.0

    if units <= 100:
        energy_charges = units * 10
    elif units <= 200:
        # First 100 units @ 10, remaining units @ 15
        energy_charges = (100 * 10) + ((units - 100) * 15)
    else:
        # First 100 @ 10, second 100 @ 15, remaining units above 200 @ 20
        energy_charges = (100 * 10) + (100 * 15) + ((units - 200) * 20)

    total_bill = energy_charges + fixed_charges

    print(f"\n--- Bill Breakdown for {units:.0f} units ---")
    print(f"Energy Charges: Rs {energy_charges:.2f}")
    print(f"Fixed Charges:  Rs {fixed_charges:.2f}")
    print(f"Total Bill:     Rs {total_bill:.2f}")
