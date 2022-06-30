#!/usr/bin/python3
"""Creation of class Rectangle"""


class Rectangle:
    """Definition the class"""

    def __init__(self, width=0, height=0):
        """Initialization of Rectangle"""

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Setting of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Requirements for width"""
        if not type(int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Setting height of rectangle"""
        return self.__height


