class Square:
    def __init__(self, size):
        self.__size = size

    def area(self):
        return self.__size ** 2

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size

