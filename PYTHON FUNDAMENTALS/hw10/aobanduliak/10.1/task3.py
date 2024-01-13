class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    @classmethod
    def print_total_employees(cls):
        return f"Total employees: {cls.total_employees}"

    def display_info(self):
        return f"Name: {self.name}, Salary: {self.salary}"

    def class_info(self):
        return f"Base classes: {Employee.__base__}, Namespace: {Employee.__dict__}, Class name: {Employee.__name__}, Module name: {Employee.__module__}, Documentation: {Employee.__doc__}"
