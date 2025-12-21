""" 
Coding Challenge 47: Level 2: Find the Minimum value of all elements in the array
"""
import sys

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
min_value = sys.maxsize

for i in range(n):
    if(arr[i]<min_value):
        min_value = arr[i]

#Alternat in built function

min_value = min(arr)

print("Minimmum value of array is : ",min_value)