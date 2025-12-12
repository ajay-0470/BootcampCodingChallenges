"""
Challenge 11: Basic Input and Salary Calculation
"""

name = input("Enter your name: ")
empID = int(input("Enter Employee ID: "))
basic_monthly_salary = float(input("Enter basic monthly salary: "))
special_allowances = float(input("Enter special allowances per month: "))
bonus = float(input("Enter annual bonus in percentage: "))


gross_monthly_salary = basic_monthly_salary + special_allowances
annual_gross_salary = (gross_monthly_salary * 12) + ((bonus * gross_monthly_salary * 12) / 100)


print(" Employee Salary Details")
print("Employee Name: ", name)
print("Employee ID: ", empID)
print("Gross Monthly Salary: ", gross_monthly_salary)
print("Annual Gross Salary: ", annual_gross_salary)
