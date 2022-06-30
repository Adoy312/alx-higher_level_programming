#!/usr/bin/python3
"""Area and Perimeter"""


class Rectangle:
    """Defines the implementation of a rectangle

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.

    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property retriever, for retreiving"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter, for setting"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property retriever, for retreiving
        the rectangle height

        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method that returns
        the rectangle area

        """
        rectangle_area = self.__height * self.__width

