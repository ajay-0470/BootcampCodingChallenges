"""
Coding Challenge 7: Program to accept name and salary. Check if their salary is >3L
and display if they must pay tax
"""

name = input("Enter your name: ")
salary = float(input("Enter your annual salary (in Lakhs): "))

if salary > 3:
    print(name, "have to pay tax.")
else:
    print(name, "does not have to pay tax.")
