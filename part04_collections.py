# ==========================================
# Name: Shah Fahad
# Roll Number: TRN-2026-000706
# Date: November 11, 2026
# Assignment: Python Mastery - Part 4
# Topic: Lists, Dictionaries, Tuples and Sets
# ==========================================

print("==========================================")
print("      PART 4: WARM-UP (Shopping List)     ")
print("==========================================")

# 1. Create initial shopping list
items = ["milk", "bread", "eggs"]
print(f"Initial list: {items}")

# 2. Append 'tea' to the list
items.append("tea")

# 3. Remove 'bread' from the list
items.remove("bread")

# 4. Sort the list alphabetically
items.sort()

# 5. Print each item with numbering using enumerate(items, start=1)
print("\nSorted Shopping List:")
for index, item in enumerate(items, start=1):
    print(f"{index}. {item}")


print("\n==========================================")
print("        PART 4: BUILD (Phone Book)        ")
print("==========================================")

# Store at least 5 contacts using a dictionary (name: phone)
phone_book = {
    "Ali": "03001234567",
    "Sara": "03129876543",
    "Usman": "03335554433",
    "Fatima": "03456677889",
    "Zain": "03211122334"
}

# Menu loop
while True:
    print("\n--- Phone Book Menu ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Show All Contacts")
    print("5. Exit")
    
    choice = input("Enter choice (1-5): ").strip()

    if choice == "1":
        name = input("Enter name: ").strip()
        number = input("Enter phone number: ").strip()
        phone_book[name] = number
        print(f"Contact '{name}' added successfully.")

    elif choice == "2":
        name = input("Enter name to search: ").strip()
        # Using .get() avoids KeyError and returns None if name does not exist
        number = phone_book.get(name)
        if number:
            print(f"Name: {name} -> Phone: {number}")
        else:
            print(f"'{name}' Not found in phone book.")

    elif choice == "3":
        name = input("Enter name to delete: ").strip()
        if name in phone_book:
            del phone_book[name]
            print(f"Contact '{name}' deleted.")
        else:
            print(f"Cannot delete. '{name}' Not found.")

    elif choice == "4":
        print("\nAll Contacts:")
        for name, number in phone_book.items():
            print(f"  {name}: {number}")

    elif choice == "5":
        print("Exiting Phone Book.")
        break
    else:
        print("Invalid choice, please select between 1 and 5.")


print("\n==========================================")
print("   PART 4: CHALLENGE (Class Result Sheet) ")
print("==========================================")

# Store student marks for 5 students across 3 subjects
results = {
    "Ali": [80, 72, 91],
    "Sara": [95, 88, 90],
    "Hamza": [35, 65, 50],   # Scored below 40 in one subject
    "Ayesha": [78, 85, 82],
    "Bilal": [28, 42, 38]    # Scored below 40 in multiple subjects
}

print("\n--- Student Results Summary ---")
student_averages = {}
below_40_students = set()  # Set stores unique names without duplicates

for name, marks in results.items():
    total = sum(marks)
    average = total / len(marks)
    student_averages[name] = average
    
    print(f"Student: {name:<8} | Total: {total} | Average: {average:.2f}")

    # Check if any subject mark is below 40
    for m in marks:
        if m < 40:
            below_40_students.add(name)

# Find class topper (student with highest average)
topper_name = max(student_averages, key=student_averages.get)
print(f"\nClass Topper: {topper_name} with an average of {student_averages[topper_name]:.2f}")

# Print set of students who scored below 40
print(f"Students with any score below 40 (Set): {below_40_students}")
