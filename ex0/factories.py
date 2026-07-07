from abc import ABC
from ex0.creatures import Creature, Flameling, Pyrodon, Aquabub, Torragon


class Creatureactory(ABC):

    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @bastractmethod
    def create_evolved(self) -> Creature:
        pass
