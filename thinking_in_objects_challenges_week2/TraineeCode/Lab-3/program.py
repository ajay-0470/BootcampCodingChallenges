from employee import Employee
from address import Address

class Program:
    @staticmethod
    def main(args):
        emp = Employee()
        Program.store_data(emp)
        Program.show_data(emp)

    @staticmethod
    def store_data(emp):
        pass

    @staticmethod
    def show_data(emp):
        # ----------------Display the employee information
        # print("Employee Id : ")
        # print("Employee Name : ")
        # print("Employee Gender : ")

        # print("Employee Address : --------------")
        # print("Address 1 : ")
        # print("Address 2 : ")
        # print("City : ")
        # print("PinCode : ")
        # print("----------------------------------")
        pass


if __name__ == "__main__":
    Program.main([])
