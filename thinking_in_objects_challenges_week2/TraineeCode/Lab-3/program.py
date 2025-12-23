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
        emp.emp_id = "E007"
        emp.name = "James Bond"
        emp.gender = "Male"

        emp.address = Address(
            addr1="25 Wellington Square,Chelsea",
            addr2= "West London",
            city = "London",
            pin_code= "SW32JX"
        )

    @staticmethod
    def show_data(emp):
        # ----------------Display the employee information
         print("Employee Id : "+emp.emp_id)
         print("Employee Name : "+ emp.name)
         print("Employee Gender : "+ emp.gender)

         print("Employee Address : --------------")
         print("Address 1 : " + emp.address.addr1)
         print("Address 2 : "+emp.address.addr2)
         print("City : "+emp.address.city)
         print("PinCode : "+emp.address.pin_code)
         print("----------------------------------")


if __name__ == "__main__":
    Program.main([])
