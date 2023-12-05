# Main program
if __name__ == "__main__":
    import sys

    # Get the number of arguments
    num_args = len(sys.argv) - 1

    # Print the number of arguments
    print("Number of argument(s):", end=" ")

    # Print "argument" or "arguments" based on the number of arguments
    if num_args == 0:
        print(".", end="\n")
    elif num_args == 1:
        print("argument:", end="\n")
    else:
        print("arguments:", end="\n")

    # Print the list of arguments with their positions
    for i in range(1, num_args + 1):
        print("{}: {}".format(i, sys.argv[i]), end="\n")
