from ex0 import FlameFactory, AquaFactory, CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")

    base_creature = factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())

    evolved_creature = factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def run_battle(factory_a: CreatureFactory, factory_b: CreatureFactory) -> None:
    """Simulates a fight between the base creatures of two factories."""
    print("Testing battle")

    creature_a = factory_a.create_base()
    creature_b = factory_b.create_base()

    print(creature_a.describe())
    print("vs.")
    print(creature_b.describe())
    print("fight!")

    print(creature_a.attack())
    print(creature_b.attack())


if __name__ == "__main__":
    # 1. Instantiate the factories
    flame_fact = FlameFactory()
    aqua_fact = AquaFactory()

    # 2. Test each factory
    test_factory(flame_fact)
    test_factory(aqua_fact)

    # 3. Simulate the battle between base creatures
    run_battle(flame_fact, aqua_fact)
