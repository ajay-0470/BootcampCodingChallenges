from salary_calculator import SalaryCalculator

class Employee:

    """
    Properties of the class
    """
    def __init__(self,emp_id="",name="",basic=0.0,hra=0.0,allowance_percentage=0.0,role=0):
        self._emp_id = str(emp_id)
        self._name = str(name)
        self._basic = float(basic)
        self._hra = float(hra)
        self._allowance_percentage = float(allowance_percentage)
        self._role = int(role)

    @property
    def emp_id(self):
        return self._emp_id

    @emp_id.setter
    def emp_id(self, value):
        self._emp_id = str(value)

    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = str(value)

    @property
    def basic(self):
        return self._basic
    
    @basic.setter
    def basic(self,value):
        self._basic = float(value)

    @property
    def hra(self):
        return self._hra

    @hra.setter
    def hra(self, value):
            self._hra = float(value)


    @property
    def allowance_percentage(self):
        return self._allowance_percentage

    @allowance_percentage.setter
    def allowance_percentage(self, value):
            self._allowance_percentage = float(value)

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
            self._role = int(value)


    def compute_allowance(self):
        return self._basic * (self._allowance_percentage / 100.0)

    def gross_salary(self):
        return self._basic + self._hra + self.compute_allowance()
    
    def __repr__(self):
        return f"Employee(Id={self._emp_id}, Name={self._name}, Basic={self._basic}, HRA={self._hra}, Allowance%={self._allowance_percentage}, Role={self._role})"

    def get_allowance(self):
        return SalaryCalculator.get_allowance(self)
    
    def get_salary(self):
        return SalaryCalculator.get_salary(self)
  