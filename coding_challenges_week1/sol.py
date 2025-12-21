"""
5, 6, 7, 9, 12, 17, 25, 38, 59, 93148, 237, 381, 614, 991
"""

n = 15         
temp = 5     

a = 1           
b = 1          

print(temp, end=", ")

for i in range(n - 1):
    temp = temp + a
    print(temp, end=", ")

    a, b = b, a + b