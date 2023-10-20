# Задача 4, О сортировке точек на плоскости

import math


def get_points(numbers, n):
    """Собирает точки из введенных чисел"""
    mas_x = []
    mas_y = []
    for i in range(0, 2 * n, 2):
        mas_x.append(numbers[i])
        mas_y.append(numbers[i+1])
    return list(zip(mas_x, mas_y))


def get_norms(points, n):
    """Считает и собирает нормы введенных чисел"""
    norms = []
    for i in range(n):
        norms.append(math.sqrt(points[i][0]**2 + points[i][1]**2))
    return norms


def sorted_points(points, n):
    """Сортирует точки в порядке неубывания нормы"""
    norms = get_norms(points, n)
    points_with_norms = list(zip(points, norms))
    return sorted(points_with_norms, key=lambda x: x[1])


n = int(input("Введите число n -> "))
numbers = list(map(float, input("Введите координаты точек через пробел: ").split()))

points = get_points(numbers, n)
for i in range(n):
    print(sorted_points(points, n)[i][0])

