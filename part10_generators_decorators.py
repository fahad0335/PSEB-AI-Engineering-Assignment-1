# ==========================================
# Name: Shah Fahad
# Roll Number: TRN-2026-000706
# Date: November 11, 2026
# Assignment: Python Mastery - Part 10
# Topic: Iterators, Generators and Decorators
# ==========================================

from functools import wraps
import os
import time

print("==========================================")
print("   PART 10: WARM-UP (Generators & Yield)  ")
print("==========================================")

# 1. Countdown generator using yield
def countdown(n: int):
    """Yield numbers from n down to 0 one by one."""
    while n >= 0:
        yield n
        n -= 1

print("Countdown from 5:")
for count in countdown(5):
    print(f"  {count}...")

# 2. Generator that yields even numbers up to limit
def evens(limit: int):
    """Yield even numbers from 0 up to limit."""
    for i in range(0, limit + 1, 2):
        yield i

# Convert evens generator to list as requested: list(evens(10)) -> [0, 2, 4, 6, 8, 10]
evens_list = list(evens(10))
print(f"\nlist(evens(10)) -> {evens_list}")


print("\n==========================================")
print("     PART 10: BUILD (Big File Reader)     ")
print("==========================================")

# Create a sample log file with 60 lines containing some ERROR lines
LOG_FILE = "server_log.txt"
with open(LOG_FILE, "w", encoding="utf-8") as f:
    for line_num in range(1, 61):
        if line_num in [7, 18, 25, 42, 53]:
            f.write(f"Line {line_num}: [ERROR] Database connection failed on port 5432\n")
        else:
            f.write(f"Line {line_num}: [INFO] Request processed successfully in 23ms\n")

# Generator 1: Read lines one by one without loading entire file into memory
def read_lines(path: str):
    """Yield lines from file one by one (stream processing)."""
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()

# Generator 2: Filter only lines containing 'ERROR'
def only_errors(lines):
    """Yield only lines containing the keyword ERROR."""
    for line in lines:
        if "ERROR" in line:
            yield line

# Stream count: count errors without building a list
lines_stream = read_lines(LOG_FILE)
errors_stream = only_errors(lines_stream)

# Count error lines using sum() generator expression (memory efficient)
error_count = sum(1 for _ in errors_stream)

print(f"Total lines in log: 60")
print(f"Total ERROR lines counted (without list): {error_count}")


print("\n==========================================")
print("   PART 10: CHALLENGE (Custom Decorators) ")
print("==========================================")

# 1. @timer decorator: measures execution duration
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        print(f"[@timer] Function '{func.__name__}' executed in {elapsed:.6f} seconds.")
        return result
    return wrapper

# 2. @log_calls decorator: logs function name and arguments
def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        params = ", ".join(args_repr + kwargs_repr)
        print(f"[@log_calls] Calling {func.__name__}({params})")
        result = func(*args, **kwargs)
        print(f"[@log_calls] {func.__name__} returned {result}")
        return result
    return wrapper

# Apply both decorators to a function that calculates sum of numbers 1 to 1,000,000
@timer
@log_calls
def sum_to_one_million(limit: int = 1_000_000) -> int:
    """Calculate the sum of numbers from 1 to 1,000,000."""
    return sum(range(1, limit + 1))

# Execute decorated function
final_sum = sum_to_one_million(1_000_000)
print(f"Resulting Sum: {final_sum}")
