"""
Module defining the interface for the display system in the game.

This module contains the `DisplayInterface` class, which provides an abstract base class
for any display implementation in the game. Any subclass of `DisplayInterface` must implement
the `update` method to handle rendering the game's display.

Classes:
    DisplayInterface: Abstract base class for display implementations.
"""

from abc import ABC, abstractmethod


class DisplayInterface(ABC):
    """
    Abstract base class for the display system in the game.

    This class defines the interface that any display implementation must follow. Subclasses
    are required to implement the `update` method to handle the rendering logic for the
    game's display.
    """

    @abstractmethod
    def update(self, player_1, player_2):
        """
        Abstract method to update the display with the current states of the players.

        This method must be implemented by any subclass to render the game's display.

        Args:
            player_1: The first player's controller with fighter attributes.
            player_2: The second player's controller with fighter attributes.

        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        raise NotImplementedError("Subclasses must implement update method.")
