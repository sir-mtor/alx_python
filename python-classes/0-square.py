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
'''
print("Size:", square1.get_size())
print("Area:", square1.area())

square1.set_size(7)

print("Updated Size:", square1.get_size())
print("Updated Area:", square1.area())
'''