#!/usr/bin/env python3

from datetime import datetime
from typing import Optional
from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContactModel(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_business_rules(self) -> "AlienContactModel":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with AC")

        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
        ):
            raise ValueError("Telepathic contact requires at least 3 witness")

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                    "Strong signals (>7.0) should include received messages"
                    )

        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("==================================")
    try:
        alien_contact = AlienContactModel(
                contact_id="AC_2024_001",
                timestamp=datetime.fromisoformat("2024-06-20T14:30:42"),
                contact_type=ContactType.radio,
                location="Area 51, Nevada",
                signal_strength=8.5,
                duration_minutes=45,
                witness_count=5,
                message_received="Greetings from Zeta Reticuli",
                is_verified=False
                )
        print("Valid contact report:")
        print(f"ID: {alien_contact.contact_id}")
        print(f"Type: {alien_contact.contact_type.value}")
        print(f"Location: {alien_contact.location}")
        print(f"Signal: {alien_contact.signal_strength}/10")
        print(f"Duration: {alien_contact.duration_minutes} minutes")
        print(f"Message: {alien_contact.message_received}")
    except ValidationError as error:
        print("===============================")
        print("\nUnexpected validation error:")
        print(error)

    try:
        AlienContactModel(
                contact_id="AC_BAD_01",
                timestamp=datetime.fromisoformat("2024-06-20T17:30:42"),
                contact_type=ContactType.telepathic,
                location="Area 42, Nevada",
                signal_strength=6.0,
                duration_minutes=45,
                witness_count=2,
                message_received=None,
                is_verified=True
                )
        print(AlienContactModel)
    except ValidationError as error:
        print("\n==================================")
        print("Expected validation error:")
        print(error)


if __name__ == "__main__":
    main()
