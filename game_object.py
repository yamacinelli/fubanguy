"""_summary_
"""

from abc import ABC
from transform import Transform


class GameObject(ABC):
    """
    docstring
    """

    def __init__(self, transform: Transform):
        self.transform = transform
        # self.start()
        # self.update()

    def start(self):
        """_summary_"""
        pass

    def update(self):
        """_summary_"""
        while True:
            self.child_update()

    def child_update(self):
        """_summary_

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError("O método child_update deve ser implementado na classe filha")
