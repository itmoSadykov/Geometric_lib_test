import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    """
    Основные тесты для функций треугольника
    """
    
    def test_area_positive(self):
        """Тест площади с положительными основанием и высотой"""
        self.assertEqual(area(10, 5), 25)
    
    def test_area_zero(self):
        """Тест площади с нулевыми основанием и высотой"""
        self.assertEqual(area(0, 5), 0)
    
    def test_perimeter_positive(self):
        """Тест периметра с положительными сторонами"""
        self.assertEqual(perimeter(3, 4, 5), 12)

if __name__ == '__main__':
    unittest.main()