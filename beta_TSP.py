from itertools import permutations
from itertools import combinations
import numpy as np


def show_mat(D):
    for k, v in D.items():
        current_string = str(k) + ((n * 3 + 2) - len(str(k))) * " "
        for j in range(n):
            current_string += " " + (str(v[j]))
        print(current_string)



graph = np.array([[np.inf, 4, 1, 3],
                  [4, np.inf, 2, 1],
                  [1, 2, np.inf, 5],
                  [3, 1, 5, np.inf]])

# graph = np.array([[np.inf, 4, 1, 3, 5],
#                   [4, np.inf, 2, 1, 5],
#                   [1, 2, np.inf, 5, 5],
#                   [3, 1, 5, np.inf, 5],
#                   [5, 5, 5, 5, np.inf]])

# graph = np.array([[np.inf, 10, 15, 20],
#                   [10, np.inf, 35, 25],
#                   [15, 35, np.inf, 30],
#                   [20, 25, 30, np.inf]])

n = len(graph[0])
vertexes = [0, 1, 2, 3]
vertex_set_list = []
for i in range(0, n + 1):
    print(len(list(combinations(vertexes, i))))
    for v in combinations(vertexes, i):
        vertex_set_list.append(list(v))
print(vertex_set_list)
print(len(vertex_set_list))

for_p = np.zeros(n)
for_d = np.zeros(n) + np.inf
P = {}
D = {}

for i in range(len(vertex_set_list)):
    print("-----------------------------набор вершин: " + str(vertex_set_list[i]))
    for_d = np.zeros(n) + np.inf
    for_p = [[] for _ in range(n)]
    if len(vertex_set_list[i]) == 1 and not vertex_set_list[i].__contains__(0):
        for_d[vertex_set_list[i]] = graph[0][vertex_set_list[i]]
        for_p[vertex_set_list[i][0]] = [0, vertex_set_list[i][0]]
    elif len(vertex_set_list[i]) == 2 and vertex_set_list[i].__contains__(0):
        for v in vertex_set_list[i]:
            if v != 0:
                for_d[0] = 2 * graph[0][v]
                for_p[0] = [v, 0]
    elif len(vertex_set_list[i]) == 2:
        print("набор вершин" + str(vertex_set_list[i]))
        for_d[vertex_set_list[i][0]] = graph[0][vertex_set_list[i][1]] + graph[vertex_set_list[i][1]][vertex_set_list[i][0]]
        for_p[vertex_set_list[i][0]] = [vertex_set_list[i][1], vertex_set_list[i][0]]
        for_d[vertex_set_list[i][1]] = graph[0][vertex_set_list[i][0]] + graph[vertex_set_list[i][0]][vertex_set_list[i][1]]
        for_p[vertex_set_list[i][1]] = [vertex_set_list[i][0],vertex_set_list[i][1]]
    elif len(vertex_set_list[i]) > 2:
        for current_vertex in vertex_set_list[i]:
            print("v = " + str(current_vertex))
            vertex_set = list(vertex_set_list[i])
            print("набор вершин" + str(vertex_set) + " без " + str(current_vertex))
            vertex_set.remove(current_vertex)
            print(vertex_set)
            vertex_set_permutations = list(permutations(vertex_set))
            print("перестановки этого набора: " + str(vertex_set_permutations))
            max = np.inf
            w_last = 0
            curr = 0
            for v in range(len(vertex_set_permutations)):
                current_permutation = list(vertex_set_permutations[v])
                print(current_permutation)
                sum = 0
                w = 0
                index_of_zero = [i for i, x in enumerate(current_permutation) if x == 0]
                print("индекс нуля: " + str(index_of_zero))
                if str(index_of_zero) != "[0]":
                    print("тут индекс нуля не ноль")
                    print("прибавляем цену пути из " + str(0) + " в " + str(current_permutation[0]))
                    sum += graph[0][current_permutation[0]]
                    for d in range(0, len(current_permutation) - 1):
                        print("прибавляем цену пути из " + str(current_permutation[d]) + " в " + str(current_permutation[d + 1]))
                        sum += graph[current_permutation[d]][current_permutation[d + 1]]
                        w = current_permutation[d + 1]
                    print("прибавляем цену пути из " + str(w) + " в " + str(current_vertex))
                    sum += graph[w][current_vertex]
                    print("предыдущий максимум: " + str(max))
                    print("сумма: " + str(sum))
                    if sum < max:
                        max = sum
                        w_last = w
                        curr = current_vertex
                        print("обновленный максимум: " + str(max))
            last_road = [w_last, curr]
            print("последнее ребро: " + str(last_road))
            for_d[current_vertex] = max
            for_p[current_vertex] = last_road
    D.update(({tuple(vertex_set_list[i]): for_d}))
    P.update(({tuple(vertex_set_list[i]): for_p}))

show_mat(D)
show_mat(P)

path = []

seen = P[tuple(vertexes)][0]
print(seen)
path.append(seen)
remember = list(path[0])
print(remember)
print(path)
for k, v in reversed(P.items()):
    print(str(n) + " " + str(len(k)))
    if len(k) < n:
        for i in range(len(v)):
            if not v[i] == [] and v[i][1] == path[(len(path) - 1)][0] and not v[i][0] in seen:
                print(str(v[i]) + " из набора " + str(k))
                print(path)
                path.append(v[i])
                seen.append(v[i][0])
                print(seen)
                print(path)
                n = len(k)
path.insert(len(path), [0, path.__getitem__(len(path)-1)[0]])
print(str(remember) + "dpfbmdfpbm")
path[0] = remember

print("оптимальный путь: " + str(list(path.__reversed__())))
sum = 0
for j in path.__reversed__():
    print(graph[j[0]][j[1]])
    sum+=graph[j[0]][j[1]]
print("сумма: " + str(sum))