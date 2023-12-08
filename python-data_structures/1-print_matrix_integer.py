def print_matrix_integer(matrix):
    for row in matrix:
        for i, element in enumerate(row):
            if i == len(row) - 1:
                # Last element in the row, no trailing space
                print("{:d}".format(element), end="")
            else:
                # Not the last element in the row, print with trailing space
                print("{:d} ".format(element), end="")
        print()

# Example usage:
matrix_example = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix_example)
