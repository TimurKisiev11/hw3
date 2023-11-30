# Задача 3, НОД чисел, введенных из консоли

import numpy as np
from functools import reduce


def gcd(a, b):
    """НОД"""
    while b:
        a, b = b, a % b
    return a


numbers = list(map(int, input("Введите НАТУРАЛЬНЫЕ числа: ").split()))
while not all(map(lambda x: x > 0, numbers)):
    numbers = list(map(int, input("введите еще раз: ").split()))

print("Ответ:")
print(reduce(lambda x, y: np.gcd(x, y), numbers))
