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

