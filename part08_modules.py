# ==========================================
# Name: Shah Fahad
# Roll Number: TRN-2026-000706
# Date: November 11, 2026
# Assignment: Python Mastery - Part 8
# Topic: Modules, Packages and Projects
# ==========================================

import datetime
import math
import os
import random
import statistics

# Import our custom module functions from school_tools.py
from school_tools import average, grade, report

print("==========================================")
print("  PART 8: WARM-UP (Standard Library Tour) ")
print("==========================================")

# 1. math: Square root of 144
sqrt_144 = math.sqrt(144)
print(f"1. math: Square root of 144 = {sqrt_144:.0f}")

# 2. random: Pick a random student from a list
students_list = ["Ali", "Sara", "Zain", "Fatima", "Hamza"]
chosen_student = random.choice(students_list)
print(f"2. random: Randomly selected student = {chosen_student}")

# 3. datetime: Calculate days left until 31 December
today = datetime.date.today()
year_end = datetime.date(today.year, 12, 31)
days_left = (year_end - today).days
print(f"3. datetime: Days left until 31 Dec ({year_end}) = {days_left} days")

# 4. statistics: Mean and median of 5 marks
sample_marks = [75, 88, 92, 60, 85]
mean_val = statistics.mean(sample_marks)
median_val = statistics.median(sample_marks)
print(f"4. statistics: Marks = {sample_marks}")
print(f"   Mean   = {mean_val:.2f}")
print(f"   Median = {median_val:.2f}")


print("\n==========================================")
print("     PART 8: BUILD (Your Own Module)      ")
print("==========================================")

print("Imported 'average', 'grade', and 'report' from school_tools.py.")
print("Notice that the test block inside school_tools.py did NOT run upon import.")

# Using the imported functions
student_marks = [88.0, 92.0, 79.0]
avg = average(student_marks)
grd = grade(avg)
rep = report("Ali Raza", student_marks)

print(f"Report from imported module: {rep}")


print("\n==========================================")
print("  PART 8: CHALLENGE (Real Project Setup)  ")
print("==========================================")

print("Checking school_app project directory layout:")
project_root = "school_app"
if os.path.exists(project_root):
    for root, dirs, files in os.walk(project_root):
        level = root.replace(project_root, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{subindent}{f}")
else:
    print(f"Folder '{project_root}' layout created.")
