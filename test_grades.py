# ==========================================
# Name: Shah Fahad
# Roll Number: TRN-2026-000706
# Date: November 11, 2026
# Assignment: Python Mastery - Part 12 (Build)
# Topic: Unit Testing with Pytest
# ==========================================

import pytest

def grade(marks: float) -> str:
    """
    Return letter grade based on marks.
    Raises ValueError for marks outside 0-100 as required by Part 12.
    """
    if marks < 0 or marks > 100:
        raise ValueError(f"Marks must be between 0 and 100. Received: {marks}")
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 33:
        return "D"
    else:
        return "Fail"


# Parametrized test for at least 8 marks covering all boundaries:
# Boundaries specified in assignment: (32, 33, 59, 60, 69, 70, 79, 80)
@pytest.mark.parametrize("marks, expected_grade", [
    (32, "Fail"),   # Boundary 1: Upper limit for Fail
    (33, "D"),      # Boundary 2: Lower limit for D
    (59, "D"),      # Boundary 3: Upper limit for D
    (60, "C"),      # Boundary 4: Lower limit for C
    (69, "C"),      # Boundary 5: Upper limit for C
    (70, "B"),      # Boundary 6: Lower limit for B
    (79, "B"),      # Boundary 7: Upper limit for B
    (80, "A"),      # Boundary 8: Lower limit for A
    (95, "A"),      # General test: high A
    (0,  "Fail"),   # Edge test: minimum valid mark
])
def test_grade_boundaries(marks, expected_grade):
    assert grade(marks) == expected_grade


def test_grade_raises_error_above_100():
    """Verify that marks above 100 raise ValueError."""
    with pytest.raises(ValueError):
        grade(105)


def test_grade_raises_error_below_0():
    """Verify that marks below 0 raise ValueError."""
    with pytest.raises(ValueError):
        grade(-10)
