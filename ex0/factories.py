from abc import ABC
from ex0.creatures import Creature, Flameling, Pyrodon, Aquabub, Torragon


class Creatureactory(ABC):

    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass

class FlameFactory(Creatureactory):

    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self):
        return Pyrodon()


class AquaFactory(Creatureactory):


    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon