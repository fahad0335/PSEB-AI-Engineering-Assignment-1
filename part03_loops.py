# ==========================================
# Name: Shah Fahad
# Roll Number: TRN-2026-000706
# Date: November 11, 2026
# Assignment: Python Mastery - Part 3
# Topic: Loops (for / while)
# ==========================================

import random

print("==========================================")
print("       PART 3: WARM-UP (Times Table)      ")
print("==========================================")

# Take a number from user
table_num = int(input("Enter a number to print its times table: "))

# Use a for loop from 1 to 10 (range(1, 11) runs up to 10)
print(f"\n--- Multiplication Table of {table_num} ---")
for i in range(1, 11):
    print(f"{table_num} x {i} = {table_num * i}")


print("\n==========================================")
print("       PART 3: BUILD (ATM PIN Check)      ")
print("==========================================")

CORRECT_PIN = "4321"
max_attempts = 3
attempts_left = max_attempts
is_authenticated = False

# Loop while attempts remain and PIN has not been verified
while attempts_left > 0:
    entered_pin = input("Enter 4-digit PIN: ")
    
    if entered_pin == CORRECT_PIN:
        print("Welcome! PIN is correct.")
        is_authenticated = True
        break  # Exit loop immediately upon successful entry
    else:
        attempts_left -= 1
        if attempts_left > 0:
            print(f"Incorrect PIN. Tries left: {attempts_left}")
        else:
            print("Card blocked! You have exceeded 3 tries.")


print("\n==========================================")
print("  PART 3: CHALLENGE (Number Guessing Game)")
print("==========================================")

while True:
    # Pick a random secret number between 1 and 50
    secret_number = random.randint(1, 50)
    guess_count = 0
    print("\nI have picked a secret number between 1 and 50. Can you guess it?")

    while True:
        user_guess = int(input("Enter your guess: "))
        guess_count += 1

        if user_guess < secret_number:
            print("Too low!")
        elif user_guess > secret_number:
            print("Too high!")
        else:
            print(f"Got it in {guess_count} guesses!")
            break

    # Ask the user if they want to play another round
    play_again = input("Play again? (y/n): ").strip().lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break


print("\n==========================================")
print("          EXTRA PRACTICE SECTION          ")
print("==========================================")

# 1. Sum of all even numbers from 1 to 100 (Expected: 2550)
even_sum = 0
for n in range(2, 101, 2):  # step=2 selects only even numbers (2, 4, 6, ..., 100)
    even_sum += n
print(f"Sum of even numbers from 1 to 100: {even_sum}")

# 2. Triangle of stars using nested loops
print("\nTriangle of stars:")
rows = 5
for r in range(1, rows + 1):
    for c in range(r):
        print("*", end=" ")
    print()  # Move to next line
