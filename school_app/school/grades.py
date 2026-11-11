# Grades calculation module

def calculate_average(marks: list[float]) -> float:
    """Calculate the average of student marks."""
    if not marks:
        return 0.0
    return sum(marks) / len(marks)

def calculate_grade(avg: float) -> str:
    """Determine letter grade from average."""
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
