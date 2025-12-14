""" 
Coding Challenge 43: Whole and Fraction value separation
Write a program to accept a double value. Separate the whole value from the fractional value and
store them in two variables. Display the same.
"""
import math

while True:
    try:
        n = float(input("Enter the double value: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer value.")

whole = math.floor(n)
fraction = n-whole

print("Whole part:", whole)
print("Fractional part:", fraction)