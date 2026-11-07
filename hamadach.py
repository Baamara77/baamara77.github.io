"""
Hamadach - Simple user category selector
A beginner Python project demonstrating input validation,
while loops, and conditional statements.
"""

print("""
====================================
             HAMADACH
====================================

Choose the category that describes you:
  1 - Student
  2 - Employee
  3 - Other
""")

valid_choices = {"1", "2", "3"}

choice = input("Enter your choice (1, 2, or 3): ").strip()

while choice not in valid_choices:
    print("Invalid choice. Please enter 1, 2, or 3.")
    choice = input("Enter your choice: ").strip()

if choice == "1":
    print("Welcome, student! ✅")
elif choice == "2":
    print("Welcome, employee! ✅")
else:
    print("Welcome! ✅")

print("Thank you for using Hamadach.")
