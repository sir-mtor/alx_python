''''
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
'''''
#!/usr/bin/python3
from sys import argv

num_args = len(argv) - 1

if num_args == 0:
    print("0 arguments.")
elif num_args == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(num_args))

for i in range(1, num_args + 1):
    print("{}: {}".format(i, argv[i]))
