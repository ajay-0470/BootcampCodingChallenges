from employee_report import EmployeeReport
from role_builder import RoleBuilder
from roles import Roles
from employee import Employee

class Program:
    @staticmethod
    def main(args):
        # Employee array to hold the employees' information
        #emp = None

        #emp_id = ""
        #name = ""
        #report_date = ""
        #basic = 0.0
        #hra = 0.0
        #role = 0

        # Accept employee information from the user
        employees = [None]*4
        print("Enter 4 employees information")

        for i in range(len(employees)):
            print("Employee No : " + str(i+1))
            emp_id = input("Id: ").strip()
            name = input("Name : ").strip()
            try:
                basic = float(input("Basic : ").strip())
            except ValueError:
                basic = 0.0

            try:
                hra = float(input("HRA : ").strip())
            except ValueError:
                hra = 0.0

            try:
                allowance_percentage = float(input("Percentage of Allowance : ").strip())
            except ValueError:
                allowance_percentage = 0.0

            print("Enter Role Id : ")
            print(str(Roles.DEVELOPER) + ". " + RoleBuilder.get_role_description(Roles.DEVELOPER))
            print(str(Roles.TEST_ENGINEER) + ". " + RoleBuilder.get_role_description(Roles.TEST_ENGINEER))
            print(str(Roles.SR_DEVELOPER) + ". " + RoleBuilder.get_role_description(Roles.SR_DEVELOPER))
            print(str(Roles.DESIGNER) + ". " + RoleBuilder.get_role_description(Roles.DESIGNER))
            role = input()

            emp = Employee(emp_id, name, basic, hra, allowance_percentage, role)
            employees[i] = emp


            employees[i] = emp

            # Note: Original C# code does not assign Employee object to Employees array

        report_date = input("Enter the date of the report (dd/mm/yyyy) : ")

        report = EmployeeReport()
        report.report_date = report_date
        report.display_employees(employees)
        input()


if __name__ == "__main__":
    import sys
    Program.main(sys.argv[1:])
