import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    """
    Основные тесты для функций круга
    """
    
    def test_area_positive(self):
        """Тест площади с положительным радиусом"""
        res = area(5)
        self.assertAlmostEqual(res, math.pi * 25, places=7)
    
    def test_area_zero(self):
        """Тест площади с нулевым радиусом"""
        res = area(0)
        self.assertEqual(res, 0)
    
    def test_perimeter_positive(self):
        """Тест длины окружности с положительным радиусом"""
        res = perimeter(5)
        self.assertAlmostEqual(res, 2 * math.pi * 5, places=7)

if __name__ == '__main__':
    unittest.main()