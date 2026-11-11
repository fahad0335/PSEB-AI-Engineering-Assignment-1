# Attendance tracking module

class AttendanceTracker:
    def __init__(self):
        self.records: dict[str, list[bool]] = {}

    def mark_attendance(self, student_name: str, present: bool) -> None:
        if student_name not in self.records:
            self.records[student_name] = []
        self.records[student_name].append(present)

    def get_percentage(self, student_name: str) -> float:
        history = self.records.get(student_name, [])
        if not history:
            return 0.0
        return (sum(history) / len(history)) * 100.0
