# ==========================================
# School Manager Package - Core Business Logic
# ==========================================

import json
import logging
import os
from typing import Dict, List, Optional
from school.models import Student

logger = logging.getLogger(__name__)

class SchoolManager:
    """Manages student records, grade calculations, rankings, and persistence."""

    def __init__(self, data_file: str = "school.json") -> None:
        self.data_file: str = data_file
        self.students: Dict[int, Student] = {}
        self.load_from_json()

    def add_student(self, name: str, roll_number: int) -> Student:
        """Add a new student if the roll number does not already exist."""
        if roll_number in self.students:
            logger.warning("Duplicate attempt: Roll number %d already exists.", roll_number)
            raise ValueError(f"Student with roll number {roll_number} already exists.")
        
        student = Student(name=name.strip(), roll_number=roll_number)
        self.students[roll_number] = student
        logger.info("Added student: %s (Roll: %d)", student.name, roll_number)
        return student

    def add_marks(self, roll_number: int, marks: List[float]) -> None:
        """Add multiple marks to an existing student."""
        student = self.get_student(roll_number)
        if not student:
            logger.error("Student with roll number %d not found.", roll_number)
            raise KeyError(f"Student with roll number {roll_number} not found.")

        for mark in marks:
            student.add_mark(mark)
        logger.info("Added %d marks to student %s.", len(marks), student.name)

    def get_student(self, roll_number: int) -> Optional[Student]:
        """Retrieve student by roll number."""
        return self.students.get(roll_number)

    def get_report_card(self, roll_number: int) -> str:
        """Generate a formatted report card string for a student."""
        student = self.get_student(roll_number)
        if not student:
            raise KeyError(f"Student with roll number {roll_number} not found.")

        marks_str = ", ".join(f"{m:.1f}" for m in student.marks) if student.marks else "No marks"
        card = [
            "================ REPORT CARD ================",
            f"Name:        {student.name}",
            f"Roll Number: {student.roll_number}",
            f"Marks:       [{marks_str}]",
            f"Average:     {student.average():.2f}",
            f"Grade:       {student.grade()}",
            "============================================="
        ]
        return "\n".join(card)

    def get_class_ranking(self) -> List[Student]:
        """
        Return students ranked by highest average first.
        Uses Python's sorted() with a lambda function.
        """
        all_students = list(self.students.values())
        ranked = sorted(all_students, key=lambda s: s.average(), reverse=True)
        return ranked

    def save_to_json(self) -> None:
        """Save all student records to JSON file."""
        data = [s.to_dict() for s in self.students.values()]
        try:
            with open(self.data_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            logger.info("Saved %d records to '%s'.", len(data), self.data_file)
        except IOError as e:
            logger.error("Failed to write to file '%s': %s", self.data_file, e)
            raise

    def load_from_json(self) -> None:
        """Load student records from JSON file if it exists."""
        if not os.path.exists(self.data_file):
            logger.info("Data file '%s' not found. Starting with empty database.", self.data_file)
            return

        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.students = {}
            for item in data:
                student = Student.from_dict(item)
                self.students[student.roll_number] = student
            logger.info("Loaded %d students from '%s'.", len(self.students), self.data_file)
        except (json.JSONDecodeError, IOError) as e:
            logger.warning("Could not read '%s' properly (%s). Starting clean.", self.data_file, e)
