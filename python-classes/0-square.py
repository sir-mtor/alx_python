class Square:

    """
    A class to represent a square.

    Attributes:
    __size (int): The size of the square.
    """

    def __init__(self, size):
         """
        Initializes a Square object with a given size.

        Parameters:
        size (int): The size of the square.
        """
     self.__size = size

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


    
       
        self.__size = size
