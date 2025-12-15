"""
Coding Challenge 48: Level 3: Find the Maximum value of all elements in the array
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
max_value = float('-inf')

for i in range(n):
    if(arr[i]>max_value):
        max_value = arr[i]

#Alternat in built function

max_value = max(arr)

print("Maximum value of array is : ",max_value)