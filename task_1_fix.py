# Задача 1, zip() через map()

zip_map_list_1 = [[1, 2, 3, -1], [1, 2]]
zip_map_list_2 = [[1, 2, 3], [2, 6]]
# zip_map_list_1 = [1, 2, 3, -1]
# zip_map_list_2 = [1, 2, 3, 2, 6]
print("первый список : " + str(zip_map_list_1))
print("второй список : " + str(zip_map_list_2))


def zip_using_map(list_1, list_2):
    return list(map(lambda x1, x2: (x1, x2), list_1, list_2))


print("зиппованный список : " + str(zip_using_map(zip_map_list_1, zip_map_list_2)))
print("для сравнения      : " + str(list(zip(zip_map_list_1, zip_map_list_2))))