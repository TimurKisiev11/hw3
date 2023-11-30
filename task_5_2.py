# Задача 5, версия 2, Стоимость поездок aka "Со словарем реально удобнее"

import numpy as np


def distribute(kilometers, prices):
    """Находит минимальную сумму всех поездок, и искомое распределение людей по машинам"""
    dir_kilometers = {i: kilometers[i] for i in range(len(kilometers))}
    dir_prices = {i: prices[i] for i in range(len(kilometers))}
    sor_dir_prices = sorted(dir_prices.items(), key=lambda x: x[1], reverse=True)  # сорт по цене в порядке убывания
    sor_dir_kilometers = sorted(dir_kilometers.items(), key=lambda x: x[1])  # сорт по расстоянию в порядке возрастания
    order_of_cars = np.zeros(len(kilometers))
    sum = 0
    for i in range(len(order_of_cars)):
        sum += sor_dir_kilometers[i][1] * sor_dir_prices[i][1]
        order_of_cars[int(sor_dir_kilometers[i][0])] = sor_dir_prices[i][0]  # по ключам восстанавливаем порядок машин
    return sum, order_of_cars


# kilometers = list(map(int, input("Введите километры ->").split()))
# kilometers = [3, 3, 3, 2, 3]
kilometers = [4, 5, 6, 1, 2, 3]
# prices = list(map(int, input("Введите цены ->").split()))
# prices = [10, 20, 1, 30, 30]
prices = [100, 150, 200, 400, 70, 95]
sum, order = distribute(kilometers, prices)

print(sum)
print(order)