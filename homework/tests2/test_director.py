import unittest
from unittest.mock import patch
from homework.tests2.ReneeMontoyaApp.models import Employee,Plant

class TestPlant(unittest.TestCase):
    @patch('models.Plant.get_file_data')
    def setUp(self, mock_get_file_data):
        mock_get_file_data.return_value = [{"id":1, "location": "Kuiv", "name": "John", "director_id": 1},
                                           {"id":2, "location": "Odesa", "name": "Mark", "director_id": 2}]

        self.employee1 = Employee(1, "James", "email@email.com", "plant", 1)
        self.plant1 = Plant(1, "Kharkiv", "Tommy", 1)

        @patch('models.Plant.get_by_id')
        def test_director(self, get_by_id_mock):
            get_by_id_mock.return_value = self.employee1
            self.assertEqual(self.plant1.director(), self.employee1)

        @patch('models.Plant.get_by_id')
        def test_director_none(self, get_by_id_mock):
            get_by_id_mock.return_value = None
            self.assertIsNone(self.plant1.director())

        @patch('models.Plant.get_file_data')
        def test_director_by_id(self, get_file_data_mock):
            get_file_data_mock.return_value = [{"id":1, "location": "Kuiv", "name": "John", "director_id": 1},
                                           {"id":2, "location": "Odesa", "name": "Mark", "director_id": 2}]
            self.assertEqual(Plant.get_plant_by_director_id(1),
                                               {"id": 1, "location": "Kuiv", "name": "John", "director_id": 1})
