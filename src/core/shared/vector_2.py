"""
vector_2.py

This module defines the Vector2 class, which represents a two-dimensional vector 
with x and y coordinates.
The class provides methods to access and modify the coordinates in an encapsulated manner.
"""


class Vector2:
    """
    Represents a vector in two dimensions.

    Attributes:
        x (float): The x-coordinate of the vector.
        y (float): The y-coordinate of the vector.
    """

    def __init__(self, x, y):
        """
        Initializes a new Vector2 object with x and y coordinates.

        Args:
            x (float): The initial x-coordinate of the vector.
            y (float): The initial y-coordinate of the vector.
        """
        self._x = x
        self._y = y

    @property
    def x(self):
        """
        Gets the x-coordinate of the vector.

        Returns:
            float: The x-coordinate of the vector.
        """
        return self._x

    @x.setter
    def x(self, value):
        """
        Sets the x-coordinate of the vector.

        Args:
            value (float): The new value for the x-coordinate.
        """
        self._x = value

    @property
    def y(self):
        """
        Gets the y-coordinate of the vector.

        Returns:
            float: The y-coordinate of the vector.
        """
        return self._y

    @y.setter
    def y(self, value):
        """
        Sets the y-coordinate of the vector.

        Args:
            value (float): The new value for the y-coordinate.
        """
        self._y = value

    def __repr__(self):
        """
        Returns a string representation of the vector.

        Returns:
            str: A string representation of the vector in the format "Vector2(x=value, y=value)".
        """
        return f"Vector2(x={self._x}, y={self._y})"
