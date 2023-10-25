#!/usr/bin/python3
"""Defining a class Square."""


class Square:
    """To Represent a square."""

    def __init__(self, size=0):
        """To Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Gets the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return current area of the square."""
        return (self.__size * self.__size)
