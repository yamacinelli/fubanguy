from abc import ABC, abstractmethod


class DisplayInterface(ABC):
    @abstractmethod
    def update(self, player_1, player_2):
        raise NotImplementedError("Subclasses must implement update method.")
