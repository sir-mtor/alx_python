class Square:
    """
    This class defines a square by a private instance attribute: size.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a new instance of the Square class.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
            size (int, optional): The size of the square. Default is 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

# Test the implementation
if __name__ == "__main__":
    my_square_1 = Square(3)
    print(type(my_square_1))
    print(my_square_1.__dict__)

    my_square_2 = Square()
    print(type(my_square_2))
    print(my_square_2.__dict__)

    try:
        print(my_square_1.size)
    except AttributeError as e:
        print(e)

    try:
        print(my_square_1.__size)
    except AttributeError as e:
        print(e)

    try:
        my_square_3 = Square("3")
        print(type(my_square_3))
        print(my_square_3.__dict__)
    except Exception as e:
        print(e)

    try:
        my_square_4 = Square(-89)
        print(type(my_square_4))
        print(my_square_4.__dict__)
    except Exception as e:
        print(e)
