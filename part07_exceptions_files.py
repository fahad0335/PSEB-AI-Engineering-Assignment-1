# ==========================================
# Name: Shah Fahad
# Roll Number: TRN-2026-000706
# Date: November 11, 2026
# Assignment: Python Mastery - Part 7
# Topic: Exceptions and Files
# ==========================================

import csv
import datetime
import json
import os

print("==========================================")
print("       PART 7: WARM-UP (Safe Division)    ")
print("==========================================")

# Keep asking until valid numbers are provided and division succeeds
while True:
    try:
        num1 = float(input("Enter first number (numerator): "))
        num2 = float(input("Enter second number (denominator): "))
        
        result = num1 / num2
        print(f"Success: {num1} / {num2} = {result:.2f}")
        break  # Exit loop after successful division

    except ValueError:
        print("Error: Invalid input! Please enter a valid number (digits only).")
    except ZeroDivisionError:
        print("Error: Division by zero is undefined! Denominator cannot be 0.")


print("\n==========================================")
print("        PART 7: BUILD (Daily Diary)       ")
print("==========================================")

DIARY_FILE = "diary.txt"

def append_diary_entry():
    today = datetime.date.today()
    note = input(f"Enter your note for today ({today}): ").strip()
    
    # Open file in append mode ('a') so existing entries are preserved
    with open(DIARY_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{today}] {note}\n")
    print("Note saved successfully.")

def view_diary_entries():
    try:
        with open(DIARY_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if content:
                print("\n--- Past Diary Entries ---")
                print(content)
            else:
                print("No entries yet.")
    except FileNotFoundError:
        print("No entries yet.")

# Simple menu for Daily Diary
while True:
    print("\n--- Daily Diary Menu ---")
    print("1. Add Today's Note")
    print("2. View All Notes")
    print("3. Done with Diary")
    choice = input("Enter choice (1-3): ").strip()

    if choice == "1":
        append_diary_entry()
    elif choice == "2":
        view_diary_entries()
    elif choice == "3":
        break
    else:
        print("Invalid choice, please select 1, 2, or 3.")


print("\n==========================================")
print("    PART 7: CHALLENGE (CSV & JSON Results)")
print("==========================================")

# Student dataset from Part 4
students_data = [
    {"name": "Ali", "marks": [80, 72, 91]},
    {"name": "Sara", "marks": [95, 88, 90]},
    {"name": "Hamza", "marks": [35, 65, 50]},
    {"name": "Ayesha", "marks": [78, 85, 82]},
    {"name": "Bilal", "marks": [28, 42, 38]}
]

# Calculate average for each student
for student in students_data:
    student["average"] = round(sum(student["marks"]) / len(student["marks"]), 2)

CSV_FILE = "results.csv"
JSON_FILE = "results.json"

# 1. Save data to results.csv
with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    # Write header
    writer.writerow(["Name", "Mark1", "Mark2", "Mark3", "Average"])
    # Write rows
    for s in students_data:
        writer.writerow([s["name"], s["marks"][0], s["marks"][1], s["marks"][2], s["average"]])

print(f"Data successfully exported to '{CSV_FILE}'.")

# 2. Save identical data to results.json
with open(JSON_FILE, "w", encoding="utf-8") as f:
    json.dump(students_data, f, indent=4)

print(f"Data successfully exported to '{JSON_FILE}'.")

# 3. Read results.csv back and determine class topper
print("\n--- Reading results.csv and Finding Topper ---")
topper_name = None
highest_avg = -1.0

with open(CSV_FILE, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row["Name"]
        avg = float(row["Average"])
        if avg > highest_avg:
            highest_avg = avg
            topper_name = name

print(f"Class Topper from CSV: {topper_name} with an average of {highest_avg:.2f}")
