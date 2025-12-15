""" 
Coding Challenge 54: Level 3: Implement Binary Search on the array.
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

arr.sort()
low = 0
high = n-1
found = False

while(low<=high):
    mid = int(low + ((high-low)/2))

    if(arr[mid]==key):
        found = True
        break
    elif(arr[mid]<key):
        low = mid+1
    else:
        high = mid-1

if(found):
    print("Element found")
else:
    print("Element not found")