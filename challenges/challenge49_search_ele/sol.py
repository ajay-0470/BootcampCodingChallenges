""" 
Coding Challenge 49: Level 4: Search the given element from the array
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

while True:
    try:
        key = int(input("Enter element to search: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer value.")

found = False

for i in range(n):
    if(arr[i]==key):
        found = True
        break

if found:
    print("Element found")
else:
    print("Element not found")