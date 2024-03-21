""" module providing a function input system """

from abc import ABC, abstractmethod


class PlayerController(ABC):
    """
    docstring
    """

    @abstractmethod
    def move_up(self):
        """
        move to up
        """
        raise ValueError("Should implement method: move_up")

    @abstractmethod
    def move_down(self):
        """
        move to down
        """
        raise ValueError("Should implement method: move_down")

    @abstractmethod
    def move_left(self):
        """
        move to left
        """
        raise ValueError("Should implement method: move_left")

    @abstractmethod
    def move_right(self):
        """
        move to right
        """
        raise ValueError("Should implement method: move_right")
