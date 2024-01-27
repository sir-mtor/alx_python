"""Module for defining an empty class BaseGeometry."""

class BaseGeometry:
    """
    A base class for geometry operations.

    This class is currently empty and serves as a base for defining
    geometric operations and properties in subclasses.
    """
    pass

# Test code
if __name__ == "__main__":
    bg = BaseGeometry()

    print(bg)
    print(dir(bg))
    print(dir(BaseGeometry))
