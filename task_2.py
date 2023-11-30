# Задача 2, Поиск минимального положительного элемента в списке


list_1 = [1, 2, 3, 4, 5, 6, 7, 0.5, -1]


def min_pos_val(list_1):
    return min(n for n in list_1 if n > 0)


print("минимальный положительный элемент в списке : " + str(list) + " равен " + str(min_pos_val(list_1)))
print("минимальный положительный элемент в списке : " + str(list) + " равен " + str(min(filter(lambda val: val > 0, list_1))))
