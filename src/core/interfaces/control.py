"""
This module defines the control interface for capturing player inputs in a fighting game.

The ControlInterface class is an abstract base class that defines methods that must be
implemented by subclasses to obtain player inputs, such as moving left, right, jumping,
and attacking.
"""

from abc import ABC, abstractmethod


class ControlInterface(ABC):
    """
    Abstract interface for capturing player inputs.

    This class defines the methods that must be implemented by subclasses to
    obtain player inputs. Each method represents an action that the player can
    perform, such as moving left, right, jumping, and attacking.
    """

    @abstractmethod
    def get_input_left(self):
        """
        Gets the input for moving left.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.

        Returns:
            bool: True if the input for moving left is active, False otherwise.
        """
        raise NotImplementedError("Subclasses must implement get_input_left method.")

    @abstractmethod
    def get_input_right(self):
        """
        Gets the input for moving right.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.

        Returns:
            bool: True if the input for moving right is active, False otherwise.
        """
        raise NotImplementedError("Should implement method: get_input_right")

    @abstractmethod
    def get_input_jump(self):
        """
        Gets the input for jumping.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.

        Returns:
            bool: True if the input for jumping is active, False otherwise.
        """
        raise NotImplementedError("Should implement method: get_input_jump")

    @abstractmethod
    def get_input_attack_1(self):
        """
        Gets the input for the first attack.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.

        Returns:
            bool: True if the input for the first attack is active, False otherwise.
        """
        raise NotImplementedError("Should implement method: get_input_attack_1")

    def get_input_attack_2(self):
        """
        Gets the input for the second attack.

        Raises:
            NotImplementedError: If the method is not implemented by the subclass.

        Returns:
            bool: True if the input for the second attack is active, False otherwise.
        """
        raise NotImplementedError("Should implement method: get_input_attack_2")
