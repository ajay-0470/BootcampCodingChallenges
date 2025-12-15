"""
Coding Challenge  16: Net Salary Calculation with Input Validation
"""


while True:
    name = input("Enter your name: ")
    if name == "":
        print("Name cannot be empty. Please re-enter.")
    elif not name.replace(" ", "").isalpha():
        print("Name must contain alphabets only. Please re-enter.")
    elif len(name) > 50:
        print("Name should not exceed 50 characters.")
    else:
        break

# Employee ID validation
while True:
    empID = input("Enter Employee ID: ")
    if not empID.isalnum():
        print("Employee ID must be alphanumeric.")
    elif len(empID) < 5 or len(empID) > 10:
        print("Employee ID must be between 5 and 10 characters.")
    else:
        break

# Basic monthly salary validation
while True:
    basic_monthly_salary = float(input("Enter basic monthly salary: "))
    if basic_monthly_salary <= 0:
        print("Basic salary must be a positive number.")
    elif basic_monthly_salary > 10000000:
        print("Basic salary exceeds allowed limit.")
    else:
        break

# Special allowances validation
while True:
    special_allowances = float(input("Enter special allowances per month: "))
    if special_allowances < 0:
        print("Special allowances cannot be negative.")
    elif special_allowances > 10000000:
        print("Special allowances exceed allowed limit.")
    else:
        break

# Bonus percentage validation
while True:
    bonus = float(input("Enter annual bonus in percentage: "))
    if bonus < 0 or bonus > 100:
        print("Bonus percentage must be between 0 and 100.")
    else:
        break



gross_monthly_salary = basic_monthly_salary + special_allowances

if gross_monthly_salary <= 0:
    print("Error: Gross Monthly Salary must be greater than zero.")
    exit()

annual_gross_salary = (gross_monthly_salary * 12) + ((bonus * gross_monthly_salary * 12) / 100)

if annual_gross_salary > 500000000:
    print("Error: Annual Gross Salary exceeds realistic value.")
    exit()

standard_deduction = 50000
taxable_income = annual_gross_salary - standard_deduction
if taxable_income < 0:
    taxable_income = 0



tax = 0
ti = taxable_income

if ti > 1500000:
    tax += (ti - 1500000) * 0.30
    ti = 1500000
if ti > 1200000:
    tax += (ti - 1200000) * 0.20
    ti = 1200000
if ti > 900000:
    tax += (ti - 900000) * 0.15
    ti = 900000
if ti > 600000:
    tax += (ti - 600000) * 0.10
    ti = 600000
if ti > 300000:
    tax += (ti - 300000) * 0.05


if taxable_income <= 700000:
    tax = 0

cess = tax * 0.04
final_tax_payable = tax + cess
net_salary = annual_gross_salary - final_tax_payable



print("Employee Salary and Tax Details")
print("Employee Name:", name)
print("Employee ID:", empID)
print("Gross Monthly Salary:", gross_monthly_salary, "Rupees")
print("Annual Gross Salary:", annual_gross_salary, "Rupees")
print("Standard Deduction:", standard_deduction, "Rupees")
print("Taxable Income:", taxable_income, "Rupees")
print("Tax Before Cess:", tax, "Rupees")
print("Health and Education Cess (4%):", cess, "Rupees")
print("Total Tax Payable:", final_tax_payable, "Rupees")
print("Annual Net Salary:", net_salary, "Rupees")
