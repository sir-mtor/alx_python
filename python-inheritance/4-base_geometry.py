"""Module for defining a class BaseGeometry."""

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

# Test code
if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
