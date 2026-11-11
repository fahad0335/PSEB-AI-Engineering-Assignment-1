"""School Management Package."""
from school.models import Student
from school.manager import SchoolManager
from school.ai_comment import make_comment, stream_comment

__all__ = ["Student", "SchoolManager", "make_comment", "stream_comment"]
