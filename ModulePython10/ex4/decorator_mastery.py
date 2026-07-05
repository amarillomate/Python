#!/usr/bin/env python3


import time
from collections.abc import Callable
from functools import wraps


def spell_timer(func: Callable[..., str]) -> Callable[..., str]:
    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        start_time= time.perf_counter()
        print(f"Casting {func.__name__}...")
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable[[Callable[..., str]], Callable[..., str]]:
    def decorator(func: Callable[..., str]) -> Callable[..., str]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            power = kwargs.get("power")
            if power is None and len(args) >= 2:
                power = args[2]
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable[[Callable[..., str]], 
                                    Callable[..., str]]:
    def decorator(func: Callable[..., str]) -> Callable[..., str]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            attempt = 1
            while attempt <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retring... "
                            f"attempt {attempt}/{max_attempts}"
                            )
                    attempt += 1
            return f"Spellcasting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(
            char.isalpha() or char.isspace() for char in name
        )

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    time.sleep(0.1)
    return "Fireball cast!"


@retry_spell(3)
def unstable_spell() -> str:
    raise RuntimeError("Spell exploded")



def main() -> None:
    print("Testing spelltimer...")
    print("Result", fireball())
    print()
    print("Testing retrying spell...")
    print(unstable_spell())
    print()
    print("Testing MageGuild...")
    print(MageGuild.validate_mage_name("Merling"))
    print(MageGuild.validate_mage_name("A1"))
    guild = MageGuild()
    print(guild.cast_spell("Lighting", 15))
    print(guild.cast_spell("Lighting", 5))


if __name__ == "__main__":
    main()
