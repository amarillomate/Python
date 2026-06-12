#!/usr/bin/env python3

import sys


def inventory_parser(inventory: dict[str, int]) -> dict[str, int]:
    for arg in sys.argv[1:]:
        if arg.count(":") != 1:
            print(f"Error - invalid parameter '{arg}'")
            continue

        parts = arg.split(":")
        tool = parts[0]
        quantity = parts[1]

        if tool in inventory:
            print(f"Redundant item '{tool}' - discarding")
            continue

        try:
            quantity_int = int(quantity)
        except ValueError as e:
            print(f"Quantity error for '{tool}': {e}")
            continue

        inventory[tool] = quantity_int

    return inventory


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = {}
    print(f"Got inventory: {inventory_parser(inventory)}")
    new_list = list(inventory.keys())
    print(f"Item list: {new_list}")
    quantity_items = sum(inventory.values())
    print(f"Total quantity of the 5 items: {quantity_items}")
    for tool, quantity in inventory.items():
        new_quantity = (quantity / quantity_items) * 100
        print(f"Item {tool} represents {round(new_quantity, 1)}%")

    most_item = ""
    most_qty = 0
    least_item = ""
    least_qty = 0

    for tool, quantity in inventory.items():
        if most_item == "":
            most_item = tool
            most_qty = quantity
            least_item = tool
            least_qty = quantity
        else:
            if quantity > most_qty:
                most_item = tool
                most_qty = quantity
            if quantity < least_qty:
                least_item = tool
                least_qty = quantity

    print(f"Item most abundant: {most_item} with quantity {most_qty}")
    print(f"Item least abundant: {least_item} with quantity {least_qty}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
