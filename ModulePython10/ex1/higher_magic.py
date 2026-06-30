#!/usr/bin/env python3

from collections.abc import Callable

Spell = Callable[[str, int], str]


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: Callable) -> Callable:
    def amplified_power(target: str, power: int) -> tuple[str, int]:
        return base_spell(target, power * multiplier)
    return amplified_power


def conditional_caster(conditional: Callable[[str, int], bool], spell: Spell) -> Spell:
    def cast_is_allowed(target: str, power: int) -> str:
        if conditional(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return cast_is_allowed


def spell_sequence(spells: list[Spell]) -> Spell:
    def cast_all(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return cast_all


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def shield(target: str, power: int) -> str:
    return f"Shield protects {target} with {power} power"


def main() -> None:
    combined = spell_combiner(fireball, heal)
    amplified = power_amplifier(fireball, 3)
    conditional = conditional_caster(lambda _target, power: power >=10, shield)
    sequence = spell_sequence([fireball, heal, shield])

    print("Testing spell combiner...")
    print(combined("Dragon", 5))

    print("Testing power amplifier...")
    print(amplified("Dragon", 5))

    print("Testing conditional caster...")
    print(conditional("Dragon", 5))
    print(conditional("Dragon", 15))

    print("Testing spell_sequence...")
    print(sequence("Dragon", 10))


if __name__ == "__main__":
    main() 
