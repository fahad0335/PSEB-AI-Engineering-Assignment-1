# ==========================================
# Name: Shah Fahad
# Roll Number: TRN-2026-000706
# Date: November 11, 2026
# Assignment: Python Mastery - Part 5
# Topic: Functions and Comprehensions
# ==========================================

import math

print("==========================================")
print("      PART 5: WARM-UP (Small Helpers)     ")
print("==========================================")

# 1. Function to calculate area of a circle (Formula: pi * r^2)
def area_of_circle(r):
    return math.pi * (r ** 2)

# 2. Function to check if a number is even (returns True or False)
def is_even(n):
    return n % 2 == 0

# 3. Greeting function with default parameter lang="en"
def greet(name, lang="en"):
    if lang == "ur":
        return f"Salaam, {name}!"
    else:
        return f"Hello, {name}!"

# Call each function three times
print("--- Calling area_of_circle 3 times ---")
print(f"Radius 3:  Area = {area_of_circle(3):.2f}")
print(f"Radius 5:  Area = {area_of_circle(5):.2f}")
print(f"Radius 10: Area = {area_of_circle(10):.2f}")

print("\n--- Calling is_even 3 times ---")
print(f"Is 4 even? {is_even(4)}")
print(f"Is 7 even? {is_even(7)}")
print(f"Is 0 even? {is_even(0)}")

print("\n--- Calling greet 3 times ---")
print(greet("Shah Fahad"))        # Uses default lang="en"
print(greet("Ali", lang="ur"))     # Uses Urdu greeting
print(greet("Sara", lang="en"))    # Uses English greeting


print("\n==========================================")
print("       PART 5: BUILD (Marks Toolkit)      ")
print("==========================================")

# 1. Calculate average of marks list
def average(marks):
    if not marks:
        return 0.0
    return sum(marks) / len(marks)

# 2. Assign grade based on average (from Part 2 grading table)
def grade(avg):
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
    else:
        return "Fail"

# 3. Generate a one-line summary report using average() and grade()
def report(name, marks):
    avg = average(marks)
    grd = grade(avg)
    return f"{name}: Avg {avg:.1f}, Grade {grd}"

# Test report function on 3 students
students_marks = {
    "Ali": [85, 90, 78],
    "Sara": [65, 70, 68],
    "Bilal": [30, 25, 40]
}

print("Student Reports:")
for student_name, marks_list in students_marks.items():
    print(" ", report(student_name, marks_list))


print("\n==========================================")
print("     PART 5: CHALLENGE (Comprehensions)   ")
print("==========================================")

# 1. Squares of 1-10 in one line using list comprehension
squares = [x ** 2 for x in range(1, 11)]
print(f"1. Squares 1-10: {squares}")

# 2. Filter names longer than 4 characters in one line
sample_names = ["Ali", "Sara", "Zainab", "Muhammad", "Umar", "Fatima"]
long_names = [name for name in sample_names if len(name) > 4]
print(f"2. Names > 4 letters: {long_names}")

# 3. Create dict of {name: average} from Part 4 results using dict comprehension
part4_results = {
    "Ali": [80, 72, 91],
    "Sara": [95, 88, 90],
    "Hamza": [35, 65, 50],
    "Ayesha": [78, 85, 82],
    "Bilal": [28, 42, 38]
}
avg_dict = {name: sum(marks) / len(marks) for name, marks in part4_results.items()}
print(f"3. Student Averages Dict: {avg_dict}")

# 4. Filter passing students only (average >= 33) in one line
passing_students = {name: round(avg, 1) for name, avg in avg_dict.items() if avg >= 33}
print(f"4. Passing Students (>= 33): {passing_students}")
