"""
Coding Challenge 14: Net Salary Calculation
Objective: Calculate annual net salary after tax deductions.
Tasks:
1. Compute Net Salary = Annual Gross Salary - Total Tax Payable.
2. Display:
o Annual Gross Salary
o Total Tax Payable (including cess)
o Annual Net Salary
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
    ti = 300000


if taxable_income <= 700000:
    tax = 0


cess = tax * 0.04
final_tax_payable = tax + cess


net_salary = annual_gross_salary - final_tax_payable


print("\nEmployee Salary and Tax Details")
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