""" 
Coding Challenge 52: Level 1: Reverse the given array.
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

print("Entered array is: ",arr)

end = n-1
start = 0

while start<end:
    arr[start],arr[end] = arr[end],arr[start]
    start+=1
    end-=1
# OR arr.reverse()
print("Reversed Array is: ",arr)