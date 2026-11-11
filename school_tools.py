# ==========================================
# Name: Shah Fahad
# Roll Number: TRN-2026-000706
# Date: November 11, 2026
# Module: school_tools.py
# Description: Helper module containing student grading functions
# ==========================================

import math

def average(marks: list[float]) -> float:
    """Calculate the average of a list of marks."""
    if not marks:
        return 0.0
    return sum(marks) / len(marks)

def grade(avg: float) -> str:
    """Return letter grade based on marks average."""
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

def report(name: str, marks: list[float]) -> str:
    """Generate a formatted one-line report for a student."""
    avg = average(marks)
    grd = grade(avg)
    return f"{name}: Avg {avg:.1f}, Grade {grd}"

# The code below only runs when school_tools.py is executed directly,
# NOT when it is imported into another file.
if __name__ == "__main__":
    print("[TEST BLOCK inside school_tools.py]")
    sample_marks = [80, 85, 90]
    print(report("Direct Test Student", sample_marks))
