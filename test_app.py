import unittest
import app


class ClassTests(unittest.TestCase):
    def test_01(self):
        result = app.get_total()
        self.assertEqual(50000005000000, result)

