"""
Coding Challenge 8: To find the largest of 3 numbers
"""
a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c = float(input("Enter 3rd number: "))

if a >= b and a >= c:
    print(a, "is the largest")
elif b >= a and b >= c:
    print(b, "is the largest")
else:
    print(c, "is the largest")