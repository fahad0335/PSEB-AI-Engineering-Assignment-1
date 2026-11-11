# ==========================================
# Name: Shah Fahad
# Roll Number: TRN-2026-000706
# Date: November 11, 2026
# Assignment: Python Mastery - Part 12
# Topic: Debugging and Testing
# ==========================================

print("==========================================")
print("         PART 12: WARM-UP (Fix 3 Bugs)    ")
print("==========================================")

"""
ORIGINAL BUGGY CODE:
-------------------
marks = [90, 25, 70]
passing = []
for m in range(len(marks) - 1):
    if marks[m] > 33:
        passing = [marks[m]]
print(sum(passing) / len(marks))

IDENTIFIED BUGS & EXPLANATIONS:
------------------------------
1. BUG 1 (Off-by-one / Boundary Error):
   'range(len(marks) - 1)' only iterates indices 0 and 1, skipping index 2 (the mark 70).
   Fix: Use 'for mark in marks:' or 'range(len(marks))'.

2. BUG 2 (Overwriting List instead of Appending):
   'passing = [marks[m]]' resets and overwrites the list each time instead of accumulating.
   Fix: Use 'passing.append(mark)'.

3. BUG 3 (Wrong Denominator in Average Calculation):
   'len(marks)' divides by total students (3) instead of passing students (2).
   Fix: Divide by 'len(passing)'.
"""

# FIXED CODE:
marks = [90, 25, 70]
passing = []

for mark in marks:
    if mark >= 33:          # Marks 33 and above are passing
        passing.append(mark)  # Append to list rather than reassigning

# Calculate average of passing marks
if passing:
    passing_average = sum(passing) / len(passing)
    print(f"Passing marks: {passing}")
    print(f"Average of passing marks (Expected 80.0): {passing_average:.1f}")
else:
    print("No passing marks found.")
