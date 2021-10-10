import unittest
from unittest.mock import patch
from employee import *

class Test_Employee(unittest.TestCase):

    def setUp(self):
        self.emp = Employee("John", "Anderson", 100)

    def test_first(self):
        self.assertEqual(self.emp.first, 'John')

    def test_last(self):
        self.assertEqual(self.emp.last, 'Anderson')

    def test_email(self):
        self.assertEqual(self.emp.email, "John.Anderson@email.com")

    def test_fullname(self):
        self.assertEqual(self.emp.fullname, "John Anderson")

    def test_apply_raise(self):
        self.assertEqual(self.emp.pay, 105)

    @patch ('employee.requests.get')
    def test_monthly_schedule(self, mocker):
        class Mocker():
            ok = True
            text = 'November schedule'

        mocker.return_value = Mocker()
        self.assertEqual(self.emp.monthly_schedule(10), "Bad response!")

if __name__ == '__main__':
    unittest.main()