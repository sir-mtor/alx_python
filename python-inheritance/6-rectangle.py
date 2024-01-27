"""Module for defining a Rectangle class."""

class BaseGeometry:
    """
    A base class for geometry operations.

    This class provides a foundation for defining geometric operations
    and properties in subclasses.
    """

    def area(self):
        """
        Compute the area of the geometry.

        Raises:
            Exception: Always raises an Exception with the message
                       "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate if the value is a positive integer.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not positive.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    This class inherits from BaseGeometry and implements methods
    specific to rectangles.
    """

    def __init__(self, width, height):
        """
        Initialize a rectangle with given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

# Test code
if __name__ == "__main__":
    try:
        r = Rectangle(0, 4)
    except ValueError as e:
        print("[ValueError]", e)
    try:
        print("Is Rectangle a subclass of BaseGeometry?", issubclass(Rectangle, BaseGeometry))
    except Exception as e:
        print("[Exception]", e)
