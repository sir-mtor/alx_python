"""
This module defines a class Square that represents a square.

The size of a square is crucial for various computations such as area computation. 
To ensure control over the type and value of the size attribute, it is kept private.

Example:
    Square = __import__('0-square').Square

    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)
"""

class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size): Initializes a Square object with the given size.
        __str__(self): Returns a string representation of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square object with the given size.

        Parameters:
            size (int): The size of the square.
        """
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A string representation of the square.
        """
        return "{} by {} by {} by {}".format(self.__size, self.__size, self.__size, self.__size)


if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)

