# Задача 1, zip() через map()

zip_map_list_1 = [[1, 2, 3, -1], [1, 2]]
zip_map_list_2 = [[1, 2, 3], [2, 6]]
print("первый список : " + str(zip_map_list_1))
print("второй список : " + str(zip_map_list_2))


def combine_to_list(a, b):
    lst = []
    list.append(lst, a)
    list.append(lst, b)
    return lst


def zip_using_map(list_1, list_2):
    return list(map(combine_to_list, list_1, list_2))


print("зиппованный список : " + str(zip_using_map(zip_map_list_1,zip_map_list_2)))
print("для сравнения      : " + str(list(zip(zip_map_list_1,zip_map_list_2))))
