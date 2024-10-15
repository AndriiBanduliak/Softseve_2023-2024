import unittest


class Worker:
    def __init__(self, name, salary=0):
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        self.name = name
        self.salary = salary

    def set_salary(self, new_salary):
        if new_salary < 0:
            raise ValueError
        self.salary = new_salary

    def get_tax_value(self):
        if self.salary <= 1000:
            tax = 0.0
        elif 1001 <= self.salary <= 3000:
            tax = 0.10 * (self.salary - 1000)
        elif 3001 <= self.salary <= 5000:
            tax = 0.10 * 2000 + 0.15 * (self.salary - 3000)
        elif 5001 <= self.salary <= 10000:
            tax = 0.10 * 2000 + 0.15 * 2000 + 0.21 * (self.salary - 5000)
        elif 10001 <= self.salary <= 20000:
            tax = 0.10 * 2000 + 0.15 * 2000 + 0.21 * \
                5000 + 0.30 * (self.salary - 10000)
        elif 20001 <= self.salary <= 50000:
            tax = 0.10 * 2000 + 0.15 * 2000 + 0.21 * 5000 + \
                0.30 * 10000 + 0.40 * (self.salary - 20000)
        else:
            tax = 0.10 * 2000 + 0.15 * 2000 + 0.21 * 5000 + 0.30 * \
                10000 + 0.40 * 30000 + 0.47 * (self.salary - 50000)

        return tax


class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.worker1 = Worker("John Doe", 800)
        self.worker2 = Worker("Jane Doe", 1001)
        self.worker3 = Worker("Bob Smith", 3001)
        self.worker4 = Worker("Joe Smith", 10000)
        self.worker5 = Worker("Bill Smith", 10001)
        self.worker6 = Worker("Clod Smith", 20001)
        self.worker7 = Worker("Arnold Smith", 50001)
        # self.worker8 = Worker("Arnold Smith", -1)

    # def tearDown(self):
    #     print('teardown')

    def test_check_0_tax(self):
        self.assertEqual(self.worker1.get_tax_value(), 0)

    def test_check_10_tax(self):
        self.assertEqual(self.worker2.get_tax_value(), 0.1)

    def test_check_15_tax(self):
        self.assertEqual(self.worker3.get_tax_value(), 200.15)

    def test_check_21_tax(self):
        self.assertEqual(self.worker4.get_tax_value(), 1550.0)

    def test_check_30_tax(self):
        self.assertEqual(self.worker5.get_tax_value(), 1550.3)

    def test_check_40_tax(self):
        self.assertEqual(self.worker6.get_tax_value(), 4550.4)

    def test_check_47_tax(self):
        self.assertEqual(self.worker7.get_tax_value(), 16550.47)

    @unittest.expectedFailure
    def test_create_worker_with_negative_salary(self):
        result = Worker("Negative Salary Worker", -100)
        self.assertEqual(result, "Salary cannot be negative")
