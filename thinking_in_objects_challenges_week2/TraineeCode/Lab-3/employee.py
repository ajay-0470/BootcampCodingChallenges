"""
Class to represent employee information
"""
from address import Address

class Employee:
    def __init__(self, emp_id='', name='', gender='', address=None):
        self.emp_id = emp_id
        self.name = name
        self.gender = gender
        self.address = address or Address()