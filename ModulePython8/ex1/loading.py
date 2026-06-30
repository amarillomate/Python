#!/usr/bin/env python3


import importlib
from importlib import metadata


def check_package(package_name: str) -> bool:
    try:
        importlib.import_module(package_name)
        version = metadata.version(package_name)
        print(f"[OK] {package_name} ({version})")
        return True
    except ImportError:
        print(f"[MISSING] {package_name}")
        return False
    except metadata.PackageNotFoundError:
        print(f"[MISSING] {package_name}")
        return False


def main() -> int:
    print("LOADING STATUS: Loading programs...")
    print()
    print("Checking dependencies:")

    pandas_ok = check_package("pandas")
    numpy_ok = check_package("numpy")
    matplotlib_ok = check_package("matplotlib")

    try:
        requests_version = metadata.version("requests")
        print(f"[OK] requests ({requests_version})")
    except metadata.PackageNotFoundError:
        print("[INFO] requests not installed (optional)")

    if not (pandas_ok and numpy_ok and matplotlib_ok):
        print()
        print("Missing required dependencies.")
        print("Install with pip:")
        print("  pip install -r requirements.txt")
        print("Install with Poetry:")
        print("  poetry install")
        return 1

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print()
    print("Analyzing Matrix data...")

    x = np.random.rand(1000)
    y = np.random.rand(1000)

    df = pd.DataFrame({
        "cycle":  x,
        "load": y,
    })

    print(f"Processing {len(df)} data points...")
    print("Generating visualization...")

    plt.figure(figsize=(10, 5))
    plt.scatter(df["cycle"], df["load"], label="Matrix load")
    plt.title("Matrix Data Analysis")
    plt.xlabel("Cycle")
    plt.ylabel("Load")
    plt.legend()
    plt.tight_layout()
    plt.savefig("matrix_analysis.png")
    plt.close()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")

    return 0


if __name__ == "__main__":
    SystemExit(main())
