#!/usr/bin/env python3

import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["Alice", "Bob", "Dylan", "Charlie"]
    actions = ["run", "grab", "sleep", "move", "swim", "climb", "walk", "eat"]

    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(
        event_list: list[tuple[str, str]]
        ) -> typing.Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        i = random.randint(0, len(event_list) - 1)
        event_remove = event_list.pop(i)
        yield event_remove


def main() -> None:
    print("=== Game Data Stream Processor ===")
    event = gen_event()
    for i in range(1000):
        player, action = next(event)
        print(f"Event {i}: Player {player} did action {action}")
    event_list: list[tuple[str, str]] = []
    for i in range(10):
        new_event = next(event)
        event_list.append(new_event)
    print(f"Built list of 10 events: {event_list}")
    for consumed_event in consume_event(event_list):
        print(f"Got event fromt list: {consumed_event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
