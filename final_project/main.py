# ==========================================
# Name: Shah Fahad
# Roll Number: TRN-2026-000706
# Date: November 11, 2026
# Assignment: Python Mastery - Final Project
# Topic: School Manager (CLI Application)
# ==========================================

import logging
import sys
from school.manager import SchoolManager
from school.ai_comment import make_comment, stream_comment

# Rule: Use logging instead of debug prints
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("school_app.log", encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("SchoolCLI")


def display_menu() -> None:
    """Print the interactive main menu."""
    print("\n===== SCHOOL MANAGER =====")
    print("1. Add student")
    print("2. Add marks")
    print("3. Show report card")
    print("4. Class ranking")
    print("5. Write comment (AI)")
    print("6. Save and exit")


def handle_add_student(manager: SchoolManager) -> None:
    """Handle adding a new student safely without crashing."""
    name = input("Enter student name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return

    try:
        roll_str = input("Enter roll number: ").strip()
        roll_number = int(roll_str)
        student = manager.add_student(name, roll_number)
        print(f"Success: Added '{student.name}' with Roll Number {student.roll_number}.")
    except ValueError as e:
        print(f"Error: {e}")


def handle_add_marks(manager: SchoolManager) -> None:
    """Handle adding marks for a student safely."""
    try:
        roll_str = input("Enter student roll number: ").strip()
        roll_number = int(roll_str)
        
        marks_input = input("Enter marks separated by spaces (e.g. 85 90 78): ").strip()
        if not marks_input:
            print("Error: No marks entered.")
            return

        marks = [float(x) for x in marks_input.split()]
        manager.add_marks(roll_number, marks)
        print(f"Success: Added {len(marks)} marks to Roll Number {roll_number}.")
    except ValueError as e:
        print(f"Input Error: Please enter valid numbers. ({e})")
    except KeyError as e:
        print(f"Not Found: {e}")


def handle_show_report_card(manager: SchoolManager) -> None:
    """Handle displaying a student's full report card."""
    try:
        roll_str = input("Enter student roll number: ").strip()
        roll_number = int(roll_str)
        report = manager.get_report_card(roll_number)
        print("\n" + report)
    except ValueError:
        print("Error: Roll number must be an integer.")
    except KeyError as e:
        print(f"Not Found: {e}")


def handle_class_ranking(manager: SchoolManager) -> None:
    """Handle displaying the class rankings sorted by average."""
    ranked_students = manager.get_class_ranking()
    if not ranked_students:
        print("No students currently registered.")
        return

    print("\n================ CLASS RANKING ================")
    print(f"{'Rank':<6}{'Roll':<8}{'Name':<16}{'Average':<10}{'Grade':<6}")
    print("-" * 46)
    for rank, student in enumerate(ranked_students, start=1):
        print(f"{rank:<6}{student.roll_number:<8}{student.name:<16}{student.average():<10.2f}{student.grade():<6}")
    print("===============================================")


def handle_write_comment(manager: SchoolManager) -> None:
    """Handle generating teacher comments with generator streaming."""
    try:
        roll_str = input("Enter student roll number: ").strip()
        roll_number = int(roll_str)
        student = manager.get_student(roll_number)
        if not student:
            print(f"Student with roll number {roll_number} not found.")
            return

        print(f"\nGenerating comment for {student.name} (streaming reply)...")
        print("Teacher Comment: ", end="", flush=True)
        for chunk in stream_comment(student):
            print(chunk, end="", flush=True)
        print()
    except ValueError:
        print("Error: Roll number must be an integer.")


def run_cli() -> None:
    """Main CLI event loop."""
    logger.info("Starting School Manager System...")
    manager = SchoolManager()

    while True:
        display_menu()
        choice = input("Choose: ").strip()

        if choice == "1":
            handle_add_student(manager)
        elif choice == "2":
            handle_add_marks(manager)
        elif choice == "3":
            handle_show_report_card(manager)
        elif choice == "4":
            handle_class_ranking(manager)
        elif choice == "5":
            handle_write_comment(manager)
        elif choice == "6":
            manager.save_to_json()
            print("Data saved successfully. Goodbye!")
            logger.info("Application shut down gracefully.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    run_cli()
