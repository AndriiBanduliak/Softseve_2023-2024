class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    @staticmethod
    def from_string(emp_str):
        firstname, lastname, salary = emp_str.split('-')
        return Employee(firstname, lastname, int(salary))


