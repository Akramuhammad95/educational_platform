from django.test import TestCase
from AtoZ.calc import Calculator

class TestCalc(TestCase):
    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(5, 3), 8)

    def test_subtract(self):
        calc = Calculator()
        self.assertEqual(calc.subtract(5, 3), 3)
