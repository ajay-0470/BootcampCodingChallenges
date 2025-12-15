""" 
Coding Challenge 46: Level 1: Find the Sum of all elements in the array
"""


while True:
    try:
        n = int(input("Enter the size of the array: "))
        if n > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter an integer value.")

arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

print(arr)

sum = 0.0

for i in range(n):
    sum +=arr[i]

print("Sum of the array is : ",sum)