
from abc import ABC, abstractmethod

class ColliderInterface(ABC):

    @abstractmethod
    def get_collision(self) -> bool:
        # TODO - doc
        raise NotImplementedError

    @abstractmethod
    def resolve_collision(self) -> None:
        # TODO - doc
        raise NotImplementedError