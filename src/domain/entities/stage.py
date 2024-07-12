"""
Module defining the Stage class.

This module provides the Stage class to represent a stage in the game, with 
attributes for background image and music.

Classes:
    Stage: Represents a stage in the game.

Usage example:
    stage = Stage("background.png", "music.mp3")
    print(stage.background_image)
    print(stage.music)
"""


class Stage:
    """
    Represents a stage in the game.

    Attributes:
        background_image (str): The background image of the stage.
        music (str): The music associated with the stage.
    """

    def __init__(self, background_image: str, music: str):
        """
        Initializes a new instance of the Stage class.

        Args:
            background_image (str): The background image of the stage.
            music (str): The music associated with the stage.
        """
        self._background_image = background_image
        self._music = music

    @property
    def background_image(self) -> str:
        """
        Gets the background image of the stage.

        Returns:
            str: The background image of the stage.
        """
        return self._background_image

    @property
    def music(self) -> str:
        """
        Gets the music associated with the stage.

        Returns:
            str: The music associated with the stage.
        """
        return self._music
