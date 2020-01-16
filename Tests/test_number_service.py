import unittest
from Services import number_service


class NumberServiceTests(unittest.TestCase):
    def test_get_list_returns_constant_number(self):
        expected_numbers = list(range(10000001))
        numbers = number_service.get_list()
        self.assertListEqual(expected_numbers, numbers)
