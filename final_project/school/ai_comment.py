# ==========================================
# School Manager Package - AI & Rule Comment Generator
# ==========================================

from functools import wraps
import time
from typing import Callable, Generator, Any
from school.models import Student

def retry(max_retries: int = 3, delay: float = 0.05) -> Callable:
    """Decorator to retry a function if a transient error occurs."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    last_exception = exc
                    time.sleep(delay)
            raise last_exception  # Re-raise if all retries failed
        return wrapper
    return decorator

@retry(max_retries=3, delay=0.05)
def fetch_ai_response(prompt: str, model_client: Any = None) -> str:
    """Simulate or call AI model with retry decorator."""
    if model_client:
        return model_client.generate(prompt)
    return "[Auto-Evaluation] Completed successfully."

def make_comment(student: Student, model_client: Any = None) -> str:
    """Generate a teacher comment based on academic performance."""
    if not student.marks:
        return "No marks recorded yet. Evaluation pending."

    avg = student.average()

    # Rule-based evaluation criteria (As required in assignment Page 11)
    if avg >= 80:
        base_comment = "Excellent in all subjects, keep it up."
    elif avg >= 70:
        base_comment = "Good performance, with room to reach top grade."
    elif avg >= 60:
        base_comment = "Fair understanding, needs more effort in challenging topics."
    elif avg >= 33:
        base_comment = "Passed, but requires dedicated revision and regular study."
    else:
        base_comment = "Needs urgent academic support and focused tutoring."

    # If external/mock model client is provided, append AI output
    if model_client:
        ai_resp = fetch_ai_response(f"Comment for {student.name} with average {avg}", model_client)
        return f"{base_comment} {ai_resp}"

    return base_comment

def stream_comment(student: Student, model_client: Any = None) -> Generator[str, None, None]:
    """Generator function that streams comment word by word (saves memory)."""
    full_text = make_comment(student, model_client=model_client)
    for word in full_text.split():
        yield word + " "
