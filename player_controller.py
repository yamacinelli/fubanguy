""" module providing a function input system """

from abc import ABC, abstractmethod


class PlayerController(ABC):
    """
    docstring
    """

    @abstractmethod
    def move_up(self, main):
        """
        move to up
        """
        raise ValueError("Should implement method: move_up")

    @abstractmethod
    def move_down(self, main):
        """
        move to down
        """
        raise ValueError("Should implement method: move_down")

    @abstractmethod
    def move_left(self, main):
        """
        move to left
        """
        raise ValueError("Should implement method: move_left")

    @abstractmethod
    def move_right(self, main):
        """
        move to right
        """
        raise ValueError("Should implement method: move_right")
