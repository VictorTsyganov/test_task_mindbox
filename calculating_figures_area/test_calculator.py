import unittest

from area_calculator import Triangle, area


class TestFigure(unittest.TestCase):
    """ Тест работы класса фигуры и дочерних классов."""

    def test_calculate_area(self):
        """ Проверка расчетов в калькуляторе."""
        test_data = {
            (2, ): 12.566370614359172,
            (4, 3, 5): 6.0,
            (4, 4, 7): 6.777720855862979,
        }
        for data, result in test_data.items():
            self.assertEqual(area(*data), result)

    def test_calculate_area_errors(self):
        """ Проверка ошибок в калькуляторе."""
        test_data = {
            (2, 3): 'Метод для данной фигуры еще не реализован.',
            (4, 3, 5, 8): 'Метод для данной фигуры еще не реализован.',
            (2, 2, 8): 'Фигура не является треугольником.',
        }
        for data, result in test_data.items():
            with self.assertRaisesRegex(ValueError, result):
                area(*data)

    def test_is_right_triangle(self):
        """ Проверка прямоугольного треугольника."""
        test_data = {
            (3, 4, 5, ): True,
            (5, 7, 8.602325267042627, ): True,
            (4, 4, 7, ): False,
        }
        for data, result in test_data.items():
            self.assertEqual((Triangle(*data).is_right_triangle())[0], result)


if __name__ == '__main__':
    unittest.main()
