"""
Coding Challenge 9: Program to check if a year given is a leap year or not
"""
year = int(input("Enter a year to check for leap year "))

if(year%400==0):
    print(str(year)+" is a leap year.")
elif(year%4==0 and year%100!=0):
        print(str(year)+" is a leap year.")
else:
      print(str(year)+" is not a leap year.")