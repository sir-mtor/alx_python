class Square:
    def __init__(self, size):
        self.__size = size

    def __str__(self):
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




''''
class Square:
#This class defines a square by its size.
    
    def __init__(self, size):
        self.__size = size

    def area(self):
        return self.__size ** 2

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size

square1 = Square(5)

#Initializes a square with a given size.
        
#Args:size (int): The size of the square.

print("Size:", square1.get_size())
print("Area:", square1.area())

square1.set_size(7)

print("Updated Size:", square1.get_size())
print("Updated Area:", square1.area())
'''