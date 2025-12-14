"""
Coding Challenge 44: Reverse of a number
Write a program to find the reverse of a number. Store the reverse value in a different variable.
Display the reverse.
"""

while True:
    try:
        num = int(input("Enter the number: "))
        break
    except ValueError:
        print("Invalid input. Please enter an number value.")

rev = 0
temp = abs(num)

while(temp>0):
    digit = temp%10
    rev = rev*10 + digit
    temp = temp//10

if(num<0):
    rev = -rev

print("Entered number: ",num)
print("Reversed number: ",rev)