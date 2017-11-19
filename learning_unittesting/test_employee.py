import unittest
from Employee_class import Employee


class TestingEmployee(unittest.TestCase):
    i = 1

    @classmethod
    def setUpClass(cls):
        print("setUpClass -> Appears at the top\n")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass -> Appears at the bottom\n")

    def setUp(self):
        self.emp_1 = Employee('Pareksha', 'Manchanda', 100)
        self.emp_2 = Employee('Bhaiya', 'Manchanda', 200)

    def tearDown(self):
        print('Test {} passed'.format(TestingEmployee.i))
        TestingEmployee.i += 1

    def test_fullname(self):
        print("Running test on fullname method")
        self.assertEqual(self.emp_1.full_name,'Pareksha Manchanda')
        self.assertEqual(self.emp_2.full_name,'Bhaiya Manchanda')

    def test_email(self):
        print('Running test on email method')
        self.assertEqual(self.emp_1.email,'pareksha.manchanda@mycompany.com')
        self.assertEqual(self.emp_2.email,'bhaiya.manchanda@mycompany.com')

    def test_raise(self):
        print('Running test on raise amount method')
        self.assertEqual(self.emp_1.apply_raise(),105)
        self.assertEqual(self.emp_2.apply_raise(),210)


if __name__ == '__main__':
    unittest.main()