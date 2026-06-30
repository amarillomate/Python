#!/usr/bin/env python3

from datetime import datetime
from typing import Optional


from pydantic import BaseModel, Field, ValidationError


class SpaceStationModel(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("SpaceStation Data Validation")
    print("==================================")
    try:
        valid_station = SpaceStationModel(
                station_id="ISS001",
                name="International Space Station",
                crew_size=6,
                power_level=85.5,
                oxygen_level=92.3,
                last_maintenance=datetime.fromisoformat("2026-06-20T14:30:25"),
                notes="Main systems stable."
                )
        print("Valid Station created:")
        print(f"ID: {valid_station.station_id}")
        print(f"Name: {valid_station.name}")
        print(f"Crew: {valid_station.crew_size} people")
        print(f"Power: {valid_station.power_level}%")
        print(f"Oxygen: {valid_station.oxygen_level}%")
        print(
                "Operational:",
                "operational" if valid_station.is_operational
                else "Not operational"
                )
    except ValidationError as error:
        print("===============================")
        print("\nUnexpected validation error:")
        print(error)

    try:
        SpaceStationModel(
                station_id="BAD01",
                name="Broken Station",
                crew_size=25,
                power_level=70.0,
                oxygen_level=88.0,
                last_maintenance=datetime.fromisoformat("2026-06-20T14:30:42")
                )
    except ValidationError as error:
        print("\n==================================")
        print("Expected validation error:")
        print(error)


if __name__ == "__main__":
    main()
