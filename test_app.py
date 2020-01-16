import unittest
import json
from app import app, get_total


class ClassTests(unittest.TestCase):
    def test_01(self):

        with app.app_context():
            response = get_total()

        response_data = json.loads(response.data)

        self.assertEqual(50000005000000, response_data['total'])

