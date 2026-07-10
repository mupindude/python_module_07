from ex0.factories import FlameFactory, AquaFactory
from ex1.factories import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
)


def run_tournament(opponents: list) -> None:
    """Executes a round-robin tournament matches based on assigned strategies."""
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    # Pre-generate base creatures for the tournament bracket to preserve performance
    match_bracket = []
    for factory, strategy in opponents:
        match_bracket.append((factory.create_base(), strategy))

    # Standard round-robin matching logic (opponent i vs opponent j)
    for i in range(len(match_bracket)):
        for j in range(i + 1, len(match_bracket)):
            creature_a, strategy_a = match_bracket[i]
            creature_b, strategy_b = match_bracket[j]

            print("* Battle *")
            print(creature_a.describe())
            print("vs.")
            print(creature_b.describe())
            print("now fight!")

            try:
                # Execute actions using the strategy contract
                strategy_a.act(creature_a)
                strategy_b.act(creature_b)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    # Instantiate Factories
    flame_fact = FlameFactory()
    aqua_fact = AquaFactory()
    heal_fact = HealingCreatureFactory()
    trans_fact = TransformCreatureFactory()

    # Instantiate Strategies
    normal_strat = NormalStrategy()
    aggressive_strat = AggressiveStrategy()
    defensive_strat = DefensiveStrategy()

    # --- Tournament 0 (Basic) ---
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    run_tournament([(flame_fact, normal_strat), (heal_fact, defensive_strat)])

    # --- Tournament 1 (Error handling validation) ---
    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    run_tournament(
        [
            (
                flame_fact,
                aggressive_strat,
            ),  # This will error out because Flameling cannot transform
            (heal_fact, defensive_strat),
        ]
    )

    # --- Tournament 2 (Multiple participants) ---
    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    run_tournament(
        [
            (aqua_fact, normal_strat),
            (heal_fact, defensive_strat),
            (trans_fact, aggressive_strat),
        ]
    )
