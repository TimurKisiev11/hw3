# Задача 5, версия 1, Стоимость поездок aka "Что такое словарь?"

from itertools import permutations
import numpy as np


def min_sum_set(kilometers, prices):
    """Выводит минимальную сумму и возвращает комбинацию цен, на которой она достигается"""
    combs_of_pr = list(permutations(prices, len(prices)))  # всевозможные комбинации цен
    curr_sum = 0.0
    min_sum = max(kilometers) * max(prices) * 10
    min_sum_set = ()
    for i in range(len(combs_of_pr)):
        for j in range(len(kilometers)):
            curr_sum += combs_of_pr[i][j] * kilometers[j]
        if curr_sum <= min_sum:
            min_sum = curr_sum
            min_sum_set = combs_of_pr[i]  # запоминаем на какой достигнута минимальная цена
            curr_sum = 0.0
        else:
            curr_sum = 0
    print(min_sum)
    return min_sum_set


def get_taxi_numbers(min_sum_set):
    """По комбинации цен составляет комбинацию номеров машин, в которые должны сесть пассажиры
    по порядку 0 1 2 3 4 5"""
    order_of_cars = np.zeros(len(min_sum_set))
    for i in range(len(min_sum_set)):
        indices_in_min_sum_set = [j for j, x in enumerate(prices) if x == min_sum_set[i]]
        indices_in_initial_prices = [j for j, x in enumerate(min_sum_set) if x == min_sum_set[i]]
        for j in range(len(indices_in_min_sum_set)):
            order_of_cars[indices_in_initial_prices[j]] = indices_in_min_sum_set[j]
    return order_of_cars


# kilometers = list(map(int, input("Введите километры ->").split()))
# kilometers = [3, 3, 3, 2, 3]
kilometers = [4, 5, 6, 1, 2, 3]
# prices = list(map(int, input("Введите цены ->").split()))
# prices = [10, 20, 1, 30, 30]
prices = [100, 150, 200, 400, 70, 95]


print(get_taxi_numbers(min_sum_set(kilometers, prices)))
