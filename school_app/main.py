# Main entry point for school_app project
from school.grades import calculate_average, calculate_grade
from school.attendance import AttendanceTracker

def main():
    print("=== Welcome to School Management App ===")
    
    # Test grades module
    marks = [85, 90, 88]
    avg = calculate_average(marks)
    grd = calculate_grade(avg)
    print(f"Student Marks: {marks} | Average: {avg:.1f} | Grade: {grd}")

    # Test attendance module
    tracker = AttendanceTracker()
    tracker.mark_attendance("Ali", True)
    tracker.mark_attendance("Ali", True)
    tracker.mark_attendance("Ali", False)
    attendance_pct = tracker.get_percentage("Ali")
    print(f"Attendance for Ali: {attendance_pct:.1f}%")

if __name__ == "__main__":
    main()
