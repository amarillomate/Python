#!/usr/bin/env python3


import time
from collections.abc import Callable
from functools import wraps


def spelltimer(func: Callable[..., str]) -> Callable[..., str]:
    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        start_time= time.perf_counter()
        print(f"Casting {func.__name__}...")
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result

    return wrapper


def powervalidator(minpower: int) -> Callable[[Callable[..., str]], Callable[..., str]]:
    def decorator(func: Callable[..., str]) -> Callable[..., str]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            power = kwargs.get("power")
            if power is None and len(args) >= 2:
                power = args[2]
            if power < minpower:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retryspell(maxattempts: int) -> Callable[[Callable[..., str]], 
                                    Callable[..., str]]:
    def decorator(func: Callable[..., str]) -> Callable[..., str]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            attempt = 1
            while attempt <= maxattempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < maxattempts:
                        print(
                            "Spell failed, retring... "
                            f"attempt {attempt}/{maxattempts}"
                            )
                    attempt += 1
            return f"Spellcasting failed after {maxattempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validatemagename(name: str) -> bool:
        return len(name) >= 3 and all(
            char.isalpha() or char.isspace() for char in name
        )

    @powervalidator(10)
    def castspell(self, spellname: str, power: int) -> str:
        return f"Successfully cast {spellname} with {power} power"


@spelltimer
def fireball() -> str:
    time.sleep(0.1)
    return "Fireball cast!"


@retryspell(3)
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
    print(MageGuild.validatemagename("Merling"))
    print(MageGuild.validatemagename("A1"))
    guild = MageGuild()
    print(guild.castspell("Lighting", 15))
    print(guild.castspell("Lighting", 5))


if __name__ == "__main__":
    main()
