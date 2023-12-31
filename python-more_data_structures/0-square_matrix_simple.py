def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    result_matrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    
    # Iterate over the rows and columns of the input matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            #square each side
            result_matrix[i][j] = matrix[i][j] ** 2
    
    return result_matrix

input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = square_matrix_simple(input_matrix)
print(result)
