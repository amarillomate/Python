#!/usr/bin/env python3

import sys
import os
import site


def is_in_virtualenv() -> bool:
    base_prefix = getattr(sys, "base_prefix", sys.prefix)
    return sys.prefix != base_prefix


def get_environment_info() -> dict[str, str]:
    info: dict[str, str] = {}
    info["python_executable"] = sys.executable
    virtual_env_path = os.environ.get("VIRTUAL_ENV", "")
    if not virtual_env_path:
        virtual_env_path = sys.prefix

    info["virtual_env_path"] = virtual_env_path
    info["virtual_env_name"] = os.path.basename(
                                virtual_env_path.rstrip(os.sep)
                                )

    try:
        site_packages = [site.getusersitepackages()]
    except AttributeError:
        site_packages = [site.getusersitepackages()]

    info["site_packages"] = ", ".join(site_packages)
    return info


def print_outside_virtualenv(info: dict[str, str]) -> None:
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {info['python_executable']}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("   python -m venv matrix_env")
    print("   source matrix_env/bin/activate # On Unix")
    print("   matrix_env\\Scripts\\activate # On Windows")
    print()
    print("Then run this program again.")


def print_inside_virtualenv(info: dict[str, str]) -> None:
    print("MATRIX STATUS: Welcome to the construct")
    print()
    print(f"Current Python: {info['python_executable']}")
    print(f"Virtual Environment: {info['virtual_env_name']}")
    print(f"Environment Path: {info['virtual_env_path']}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")
    print()
    print(f"Package installation path: {info['site_packages']}")


def main() -> None:
    info = get_environment_info()

    if is_in_virtualenv():
        print_inside_virtualenv(info)
    else:
        print_outside_virtualenv(info)


if __name__ == "__main__":
    main()
