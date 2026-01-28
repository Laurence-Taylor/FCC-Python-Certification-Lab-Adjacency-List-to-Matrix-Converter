def adjacency_list_to_matrix(adj_list):
    matrix_len = len(adj_list)
    matrix_to_return = [[0 for _ in range(matrix_len)] for _ in range(matrix_len)]
    i = 0
    j = 0
    for key, list_edge in adj_list.items():
        for value in list_edge:
            matrix_to_return[i][value]=1
        i += 1
    print(matrix_to_return)

if __name__ == '__main__':
    adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]})