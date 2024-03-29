"""
This module defines the Square class.

The Square class inherits from the Rectangle class and represents a square shape.
"""
from models.rectangle import Rectangle
"""Initializes a Square instance."""
       
class Square(Rectangle):
     """
    This class represents a square shape.

    It inherits from the Rectangle class and shares its attributes and methods.
    """
     def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

     def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
     @property
     def size(self):
        return self.width

     @size.setter
     def size(self, value):
        self.width = value
        self.height = value