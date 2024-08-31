# tests/test_calculator.py

import unittest
from calculator import Calculator  # Asegúrate de que este import sea correcto

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Se ejecuta antes de cada método de prueba."""
        self.calc = Calculator()

    def test_addition(self):
        """Prueba la función de suma."""
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_subtraction(self):
        """Prueba la función de resta."""
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiplication(self):
        """Prueba la función de multiplicación."""
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_division(self):
        """Prueba la función de división."""
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_division_by_zero(self):
        """Prueba la división por cero."""
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
