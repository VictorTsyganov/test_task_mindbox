# Напишите на C# или Python библиотеку для поставки внешним клиентам,
# которая умеет вычислять площадь круга по радиусу и треугольника по трем сторонам.
from math import sqrt, pi


class Figure:
    """ Базовый класс."""

    def calculate_area(self):
        pass


class Circle(Figure):
    """ Класс для кгугов."""

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius**2


class Triangle(Figure):
    """ Класс треугольников."""

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        """ Является ли фигура треугольником."""
        if (self.a + self.b > self.c
            and self.a + self.c > self.b
                and self.b + self.c > self.a):
            return True
        raise ValueError('Фигура не является треугольником.')

    def is_right_triangle(self):
        """ Является ли треугольник прямоугольным."""
        sides = sorted(list([self.a, self.b, self.c]))
        if sides[2]**2 == sides[0]**2 + sides[1]**2:
            return True, sides
        return False, sides

    def calculate_area(self):
        """ Расчет площади треугольника."""
        if self.is_triangle():
            if self.is_right_triangle()[0]:
                sides = self.is_right_triangle()[1]
                return (sides[0] * sides[1])/2
            p = (self.a + self.b + self.c) / 2
            return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


def area(*args):
    if len(args) == 1:
        return Circle(*args).calculate_area()
    if len(args) == 3:
        return Triangle(*args).calculate_area()
    if len(args) == 2 or len(args) > 3:
        raise ValueError('Метод для данной фигуры еще не реализован.')


if __name__ == '__main__':
    list_input = list(map(float, input(
        'Введите радиус круга или стороны треугольника через пробел :')
        .split()))
    print(area(*list_input))
