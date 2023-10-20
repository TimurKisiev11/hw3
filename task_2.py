# Задача 2, Поиск минимального положительного элемента в списке


list = [1, 2, 3, 4, 5, 6, 7, 0.5, -1]


def min_pos_val(list):
    return min(n for n in list if n > 0)


print("минимальный положительный элемент в списке : " + str(list) + " равен " + str(min_pos_val(list)))
