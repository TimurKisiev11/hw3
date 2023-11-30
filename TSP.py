from itertools import permutations
from itertools import combinations
import numpy as np



def show_mat(D, n):
    for k, v in D.items():
        current_string = str(k) + ((n * 3 + 2) - len(str(k))) * " "
        current_string += " ".join(str(val) for val in v)
        print(current_string)


def get_ver_sets(n):
    vertexes = [i for i in range(0, n)]
    vertex_set_list = [list(v) for i in range(0, n + 1) for v in combinations(vertexes, i)]
    return vertex_set_list


def get_D_P(graph):
    D = {}
    P = {}
    n = len(graph[0])
    vertex_set_list = get_ver_sets(n)
    for i in range(len(vertex_set_list)):
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
            for_d[vertex_set_list[i][0]] = graph[0][vertex_set_list[i][1]] + graph[vertex_set_list[i][1]][vertex_set_list[i][0]]
            for_p[vertex_set_list[i][0]] = [vertex_set_list[i][1], vertex_set_list[i][0]]
            for_d[vertex_set_list[i][1]] = graph[0][vertex_set_list[i][0]] + graph[vertex_set_list[i][0]][vertex_set_list[i][1]]
            for_p[vertex_set_list[i][1]] = [vertex_set_list[i][0], vertex_set_list[i][1]]
        elif len(vertex_set_list[i]) > 2:
            for current_vertex in vertex_set_list[i]:
                current_vertex_set = list(vertex_set_list[i])
                current_vertex_set.remove(current_vertex)
                vertex_set_permutations = list(permutations(current_vertex_set))
                max = np.inf
                last_edge = []
                for current_permutation in vertex_set_permutations:
                    sum = 0
                    w = 0
                    index_of_zero = [i for i, x in enumerate(current_permutation) if x == 0]
                    if index_of_zero != [0]:
                        sum += graph[0][current_permutation[0]]
                        for d in range(0, len(current_permutation) - 1):
                            sum += graph[current_permutation[d]][current_permutation[d + 1]]
                            w = current_permutation[d + 1]
                        sum += graph[w][current_vertex]
                        if sum < max:
                            max = sum
                            last_edge = [w, current_vertex]
                for_d[current_vertex] = max
                for_p[current_vertex] = last_edge
        D.update(({tuple(vertex_set_list[i]): for_d}))
        P.update(({tuple(vertex_set_list[i]): for_p}))
    return D, P


def get_optimal_path(P, n):
    seen = P[tuple([i for i in range(0, n)])][0]
    optimal_path = [list(seen)]
    remember = optimal_path[0]
    for cur_set, edges in reversed(P.items()):
            for i in range(len(edges)):
                if len(cur_set) < n and not edges[i] == [] and edges[i][1] == optimal_path[(len(optimal_path) - 1)][0] and not edges[i][0] in seen:
                    optimal_path.append(edges[i])
                    seen.append(edges[i][0])
                    n = len(cur_set)
    optimal_path.insert(len(optimal_path), [0, optimal_path[(len(optimal_path) - 1)][0]])
    optimal_path[0] = remember
    return optimal_path

graph_1 = np.array([[np.inf, 4, 1, 3],
                    [4, np.inf, 2, 1],
                    [1, 2, np.inf, 5],
                    [3, 1, 5, np.inf]])

graph_2 = np.array([[np.inf, 4, 1, 3, 5],
                    [4, np.inf, 2, 1, 5],
                    [1, 2, np.inf, 5, 5],
                    [3, 1, 5, np.inf, 5],
                    [5, 5, 5, 5, np.inf]])

graph_3 = np.array([[np.inf, 10, 15, 20],
                    [10, np.inf, 35, 25],
                    [15, 35, np.inf, 30],
                    [20, 25, 30, np.inf]])

graph = graph_1

D, P = get_D_P(graph)
show_mat(D, len(graph[0]))
show_mat(P, len(graph[0]))

optimal_path = get_optimal_path(P, len(graph[0]))
print("Оптимальный путь: " + str(list(reversed(optimal_path))))
sum = 0
for j in reversed(optimal_path):
    print(graph[j[0]][j[1]])
    sum += graph[j[0]][j[1]]
print("сумма: " + str(sum))
