class Square:
    """
    This class defines a square by a private instance attribute: size.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size): Initializes a new instance of the Square class.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Parameters:
            size (int): The size of the square.
        """
        self.__size = size

# Test the implementation
if __name__ == "__main__":
    my_square = Square(3)

    # Print type and dictionary representation of the object
    print(type(my_square))
    print(my_square.__dict__)

    # Try accessing size and __size (should raise AttributeError)
    try:
        print(my_square.size)
    except AttributeError as e:
        print(e)

    try:
        print(my_square.__size)
    except AttributeError as e:
        print(e)
