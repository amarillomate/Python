import alchemy
from elements import create_fire


def lead_to_gold() -> str:
    air = alchemy.create_air()
    strength = alchemy.strength_potion()
    fire = create_fire()
    return (
            "Recipe transmuting Lead to"
            f" Gold: brew {air} and {strength}"
            f"mixed with {fire}"
            )
