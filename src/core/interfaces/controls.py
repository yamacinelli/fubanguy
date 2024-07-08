from abc import ABC, abstractmethod


class GameControls(ABC):
    @abstractmethod
    def get_input(self):
        pass
