def adjacency_list_to_matrix(adj_list):
    # Determine the number of nodes
    matrix_len = len(adj_list)
    # Create a new Matrix with all values in 0
    matrix_to_return = [[0 for _ in range(matrix_len)] for _ in range(matrix_len)]
    # counter of nodes
    i = 0
    # for each dictioanry key value pair (items)
    for key, list_edge in adj_list.items():
        # for each value in the list
        for value in list_edge:
            matrix_to_return[i][value]=1
        # print matrix row
        print(matrix_to_return[i])
        # next node
        i += 1
    # return matix
    return matrix_to_return

if __name__ == '__main__':
    adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]})