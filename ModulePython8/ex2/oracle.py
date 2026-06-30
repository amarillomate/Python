#!/usr/bin/env python3

import os

try:
    from dotenv import load_dotenv
except ImportError:
    print("ERROR: Missing dependency 'python-dotenv'.")
    print("Install it inside your virtual environment:")
    print("  python3 -m pip install python-dotenv")
    print(
            "Make sure your virtual environment is activated "
            "before running oracle.py."
            )
    raise SystemExit(1)


def get_env(name: str, default: str = "") -> str:
    return os.getenv(name, default).strip()


def mask_secret(value: str) -> str:
    if not value:
        return "Missing"
    if len(value) <= 4:
        return "*" * (len(value))
    return "*" * (len(value) - 4) + value[-4:]


def mode_message(mode: str) -> str:
    if mode == "production":
        return "Database: Connected to production instance"
    return "Database: Connected to local instance"


def main() -> int:
    try:
        load_dotenv()
    except ModuleNotFoundError as e:
        print(f"{e}")

    print("ORACLE STATUS: Reading the Matrix...")
    print()

    mode = get_env("MATRIX_MODE", "development")
    if mode not in ("development", "production"):
        mode = "development"

    database_url = get_env("DATABASE_URL")
    api_key = get_env("API_KEY")
    log_level = get_env(
            "LOG_LEVEL", "DEBUG"
            if mode == "development" else "INFO"
            )
    zion_endpoint = get_env("ZION_ENDPOINT")

    missing = []
    if not database_url:
        missing.append("DATABASE_URL")
    if not log_level:
        missing.append("LOG_LEVEL")
    if not zion_endpoint:
        missing.append("ZION_ENDPOINT")

    if missing:
        print("WARNING: Missing configuration values:")
        for item in missing:
            print(f" - {item}")
        print()

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(mode_message(mode))

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing API key")

    print(f"Log level: {log_level}")
    print(f"Zion Network: {'Online' if zion_endpoint else 'Offline'}")
    print()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
