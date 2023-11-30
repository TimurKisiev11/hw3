# Задача 1, zip() через map()

# zip_map_list_1 = [[1, 2, 3, -1], [1, 2]]
# zip_map_list_2 = [[1, 2, 3], [2, 6]]
# zip_map_list_3 = [[7, 8, 9], [3, 7]]
zip_map_list_1 = [1, 2, 3, -1]
zip_map_list_2 = [1, 2, 3, 2, 6]
zip_map_list_3 = [1, 2, 3, 2, 6]
print("первый список : " + str(zip_map_list_1))
print("второй список : " + str(zip_map_list_2))


def zip_using_map(*args):
    return list(map(lambda *x: x, *args))


print("зиппованный список : " + str(zip_using_map(zip_map_list_1, zip_map_list_2, zip_map_list_3)))
print("для сравнения      : " + str(list(zip(zip_map_list_1, zip_map_list_2, zip_map_list_3))))