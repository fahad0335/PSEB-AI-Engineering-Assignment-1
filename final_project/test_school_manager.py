# ==========================================
# Name: Shah Fahad
# Roll Number: TRN-2026-000706
# Date: November 11, 2026
# Final Project - Pytest Test Suite
# Tests: Student Dataclass, Manager, JSON Persistence, Exceptions & AI Mocking
# ==========================================

import os
import pytest
from school.models import Student
from school.manager import SchoolManager
from school.ai_comment import make_comment, stream_comment


def test_student_creation_and_validation():
    s = Student(name="Ali", roll_number=101)
    assert s.name == "Ali"
    assert s.roll_number == 101
    assert s.marks == []

    # Invalid empty name
    with pytest.raises(ValueError):
        Student(name="", roll_number=102)

    # Invalid non-positive roll number
    with pytest.raises(ValueError):
        Student(name="Sara", roll_number=-5)


def test_add_mark_and_average():
    s = Student(name="Sara", roll_number=102)
    s.add_mark(80.0)
    s.add_mark(90.0)
    s.add_mark(70.0)
    assert s.average() == 80.0
    assert s.grade() == "A"

    # Mark out of bounds
    with pytest.raises(ValueError):
        s.add_mark(150.0)
    with pytest.raises(ValueError):
        s.add_mark(-10.0)


def test_report_card_generation(tmp_path):
    temp_file = str(tmp_path / "test_school.json")
    mgr = SchoolManager(data_file=temp_file)
    mgr.add_student("Zain", 103)
    mgr.add_marks(103, [75.0, 85.0])
    
    report = mgr.get_report_card(103)
    assert "Zain" in report
    assert "Roll Number: 103" in report
    assert "Average:     80.00" in report
    assert "Grade:       A" in report


def test_class_ranking_order(tmp_path):
    temp_file = str(tmp_path / "test_school.json")
    mgr = SchoolManager(data_file=temp_file)
    
    mgr.add_student("Ali", 1)
    mgr.add_marks(1, [60, 60])  # avg = 60

    mgr.add_student("Sara", 2)
    mgr.add_marks(2, [90, 95])  # avg = 92.5 (Topper)

    mgr.add_student("Hamza", 3)
    mgr.add_marks(3, [75, 80])  # avg = 77.5

    ranked = mgr.get_class_ranking()
    assert ranked[0].name == "Sara"
    assert ranked[1].name == "Hamza"
    assert ranked[2].name == "Ali"


def test_json_save_and_load(tmp_path):
    temp_file = str(tmp_path / "test_school.json")
    mgr1 = SchoolManager(data_file=temp_file)
    mgr1.add_student("Fatima", 201)
    mgr1.add_marks(201, [88, 92])
    mgr1.save_to_json()

    mgr2 = SchoolManager(data_file=temp_file)
    loaded_student = mgr2.get_student(201)
    assert loaded_student is not None
    assert loaded_student.name == "Fatima"
    assert loaded_student.marks == [88.0, 92.0]
    assert loaded_student.average() == 90.0


def test_invalid_operations_exception_handling(tmp_path):
    temp_file = str(tmp_path / "test_school.json")
    mgr = SchoolManager(data_file=temp_file)
    mgr.add_student("Bilal", 301)

    # Duplicate roll number
    with pytest.raises(ValueError):
        mgr.add_student("Bilal Duplicate", 301)

    # Non-existent student
    with pytest.raises(KeyError):
        mgr.add_marks(999, [50, 60])

    with pytest.raises(KeyError):
        mgr.get_report_card(999)


class MockAIModel:
    """Mock AI model for offline pytest runs."""
    def generate(self, prompt: str) -> str:
        return "[Mock AI] Demonstrates remarkable grasp of course material."


def test_ai_comment_with_mock_model():
    student = Student(name="Ayesha", roll_number=401, marks=[95, 90, 92])
    mock_model = MockAIModel()

    comment = make_comment(student, model_client=mock_model)
    assert "Excellent in all subjects" in comment
    assert "[Mock AI]" in comment

    chunks = list(stream_comment(student, model_client=mock_model))
    assert len(chunks) > 0
    full_streamed_text = "".join(chunks).strip()
    assert full_streamed_text == comment
