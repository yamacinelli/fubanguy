"""
This module contains the PlayingTimePresenter class, responsible for
handling the logic of updating and managing the playing time.
"""


class PlayingTimePresenter:
    """
    A presenter for managing the playing time in the game.

    This class processes time-related updates and informs the view
    to update its display accordingly.
    """

    def __init__(self, initial_time: int):
        """
        Initializes the PlayingTimePresenter with an initial time.

        Args:
            initial_time (int): The initial time for the countdown in seconds.
        """
        self.initial_time = initial_time
        self.elapsed_time = 0

    def on_time_update(self, delta_time: int):
        """
        Updates the elapsed time and processes the logic for updating the view.

        Args:
            delta_time (int): The amount of time that has passed since the last update.
        """
        self.elapsed_time += delta_time

    def get_remaining_time(self) -> int:
        """
        Returns the remaining time in the countdown.

        Returns:
            int: The remaining time in seconds.
        """
        return self.initial_time - self.elapsed_time
