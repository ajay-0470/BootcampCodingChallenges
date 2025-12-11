x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Before swapping:")
print("First number is", x)
print("Second number is", y)

temp = x
x = y
y = temp

print("After swapping:")
print("First number is", x)
print("Second number is", y)