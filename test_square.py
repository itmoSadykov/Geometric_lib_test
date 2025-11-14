import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    """
    Основные тесты для функций квадрата
    """
    
    def test_area_positive(self):
        """Тест площади с положительной стороной"""
        self.assertEqual(area(5), 25)
    
    def test_area_zero(self):
        """Тест площади с нулевой стороной"""
        self.assertEqual(area(0), 0)
    
    def test_perimeter_positive(self):
        """Тест периметра с положительной стороной"""
        self.assertEqual(perimeter(5), 20)

if __name__ == '__main__':
    unittest.main()