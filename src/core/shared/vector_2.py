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
        """Gets the x-coordinate of the vector."""
        return self._x

    @x.setter
    def x(self, value):
        """Sets the x-coordinate of the vector."""
        self._x = value

    @property
    def y(self):
        """Gets the y-coordinate of the vector."""
        return self._y

    @y.setter
    def y(self, value):
        """Sets the y-coordinate of the vector."""
        self._y = value

    def __repr__(self):
        """Returns a string representation of the vector in tuple format."""
        return f"({self._x}, {self._y})"

    def __iter__(self):
        """Allows the Vector2 object to be iterated as (x, y)."""
        yield self._x
        yield self._y
