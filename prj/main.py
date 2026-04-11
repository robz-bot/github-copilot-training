#!/usr/bin/env python3

import textwrap


def show_landing_page() -> None:
    banner = r"""
  ____        _   _                 _     ____            _
 |  _ \ _   _| |_| |__   ___  _ __ | |_  |  _ \ ___  __ _| |_ ___
 | |_) | | | | | __| '_ \ / _ \| '_ \| __| | |_) / _ \/ _` | __/ _ \
 |  __/| |_| | |_| | | | (_) | | | | |_  |  __/  __/ (_| | ||  __/
 |_|    \__, |\__|_| |_|\___/|_| |_|\__| |_|   \___|\__,_|\__\___|
        |___/
"""
    print(banner)
    print("Welcome to the Python Project")
    print("A lightweight, friendly starting point for building your next idea.")
    print()
    print("What this app does:")
    print(" - Shows an engaging landing screen in the terminal")
    print(" - Prints a greeting once you continue")
    print()
    print(textwrap.fill("Customize this landing page with your own project name, description, and actions. "
                        "Keep it simple, readable, and welcoming.", width=72))
    print()
    input("Press Enter to continue...")
    print()


def main() -> None:
    show_landing_page()
    print("Hello, World!")


if __name__ == "__main__":
    main()
