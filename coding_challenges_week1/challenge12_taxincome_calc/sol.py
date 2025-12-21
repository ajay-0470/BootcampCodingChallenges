"""
Coding Challenge 12: Taxable Income Calculation
Objective: Calculate taxable income after standard deductions.
Tasks:
• Deduct a Standard Deduction of ₹50,000 from the annual gross salary.
• Compute the Taxable Income and display all intermediate calculations.
Output: Display gross salary, standard deduction and taxable income.
"""

name = input("Enter your name: ")
empID = int(input("Enter Employee ID: "))
basic_monthly_salary = float(input("Enter basic monthly salary: "))
special_allowances = float(input("Enter special allowances per month: "))
bonus = float(input("Enter annual bonus in percentage: "))


gross_monthly_salary = basic_monthly_salary + special_allowances

annual_gross_salary = (gross_monthly_salary * 12) + ((bonus * gross_monthly_salary * 12) / 100)


standard_deduction = 50000
taxable_income = annual_gross_salary - standard_deduction


print(" Employee Salary & Taxable Income Detail")
print("Employee Name: ", name)
print("Employee ID: ", empID)
print("Gross Monthly Salary: ", gross_monthly_salary)
print("Annual Gross Salary: ", annual_gross_salary)
print("Standard Deduction: ", standard_deduction)
print("Taxable Income: ", taxable_income)
