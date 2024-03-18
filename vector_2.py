"""_summary_

Returns:
    _type_: _description_
"""

import dataclasses


@dataclasses.dataclass
class Vector2:
    """_summary_"""

    def __init__(self, x, y) -> None:
        """
        docstring
        """
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        """Getter to get the attribute value."""
        return self._x

    @x.setter
    def x(self, value):
        """Setter to set the attribute value."""
        self._x = value

    @property
    def y(self) -> int:
        """Getter to get the attribute value."""
        return self._y

    @y.setter
    def y(self, value):
        """Setter to set the attribute value."""
        self._y = value
