import unittest
from unittest.mock import patch
from homework.tests2.ReneeMontoyaApp.models import Employee, Plant


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee(1, 'Test Tester', 'test@test.com', 'plant', 1)

    def test_generate_dict(self):
        self.assertIn('id', self.employee._generate_dict())
        self.assertEqual(self.employee._generate_dict()['id'], 1)
        self.assertEqual(self.employee._generate_dict()['department_type'], 'plant')

    @patch('models.Employee.get_file_data')
    def test_get_by_id(self, fileDataMock):
        fileDataMock.return_value = [{"id": 1, "email": "lubomur.luzhnuy@gmail.com", "name": "Liubomyr Luzhnyi", "department_type": "plant", "department_id": 1}]
        self.assertEqual(self.employee.get_by_id(1)['email'], "lubomur.luzhnuy@gmail.com")
        self.assertIn('id', self.employee.get_by_id(1))


    @patch('models.Employee.get_by_id')
    def test_department(self, get_by_id_mock):
        get_by_id_mock.return_value = self.plant
        self.assertEqual(self.employee.department(), self.plant)

    @patch('models.Employee.get_by_id')
    def test_departyment_none(selfs, get_by_id_mock):
        get_by_id_mock.return_value = None
        self.assertIsNone(self.employee.department(), self.plant)