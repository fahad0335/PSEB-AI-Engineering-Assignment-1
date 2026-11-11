# ==========================================
# School Manager Package - Student Model
# ==========================================

from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class Student:
    """Student dataclass representing a school student."""
    name: str
    roll_number: int
    marks: List[float] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Validate student fields on creation."""
        if not self.name or not self.name.strip():
            raise ValueError("Student name cannot be empty.")
        if self.roll_number <= 0:
            raise ValueError("Roll number must be a positive integer.")
        for m in self.marks:
            if m < 0 or m > 100:
                raise ValueError(f"Marks must be between 0 and 100. Invalid: {m}")

    def add_mark(self, mark: float) -> None:
        """Add a single mark after validation."""
        if mark < 0 or mark > 100:
            raise ValueError(f"Mark must be between 0 and 100. Received: {mark}")
        self.marks.append(mark)

    def average(self) -> float:
        """Calculate average of all marks."""
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)

    def grade(self) -> str:
        """Determine grade from average."""
        if not self.marks:
            return "N/A"
        avg = self.average()
        if avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 33:
            return "D"
        else:
            return "Fail"

    def to_dict(self) -> Dict[str, Any]:
        """Convert Student object to dictionary for JSON persistence."""
        return {
            "name": self.name,
            "roll_number": self.roll_number,
            "marks": self.marks
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Student":
        """Instantiate a Student object from a dictionary."""
        return cls(
            name=data["name"],
            roll_number=int(data["roll_number"]),
            marks=[float(m) for m in data.get("marks", [])]
        )
