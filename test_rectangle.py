import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    """
    Основные тесты для функций прямоугольника
    """
    
    def test_zero_mul(self):
        """Тест площади с нулевой стороной"""
        res = area(10, 0)
        self.assertEqual(res, 0)
        
    def test_square_mul(self):
        """Тест площади квадратного прямоугольника"""
        res = area(10, 10)
        self.assertEqual(res, 100)
    
    def test_perimeter_positive(self):
        """Тест периметра с положительными сторонами"""
        self.assertEqual(perimeter(5, 10), 30)

if __name__ == '__main__':
    unittest.main()