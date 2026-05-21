#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}C is too cold for plants (min 0C)")
    elif temp > 40:
        raise ValueError(f"{temp}C is too hot for plants (max 40C)")
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print("Input data is '25'")
    try:
        res1 = input_temperature("25")
        print(f"Temperature is now {res1}C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()
    print("Input data is 'abc'")
    try:
        res2 = input_temperature("abc")
        print(f"Temperature is now {res2}C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()
    print("Input data is '100'")
    try:
        res3 = input_temperature("100")
        print(f"Temperature is now {res3}C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()
    print("Input data is '-50'")
    try:
        res4 = input_temperature("-50")
        print(f"Temperature is now {res4}C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
