#!/usr/bin/env python3

import random
import sys
import textwrap
import time


def chaotic_print(lines, delay=0.08, jitter=0.06):
    for line in lines:
        print(line)
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-jitter, jitter))


def show_landing_page() -> None:
    banners = [
        r"""
   _____ _           _   _             ____  _                 
  / ____| |         | | (_)           |  _ \(_)                
 | |    | |__   __ _| |_ _  ___  _ __ | |_) |_  ___  _ __  ___ 
 | |    | '_ \ / _` | __| |/ _ \| '_ \|  _ <| |/ _ \| '_ \/ __|
 | |____| | | | (_| | |_| | (_) | | | | |_) | | (_) | | | \__ \
  \_____|_| |_|\__,_|\__|_|\___/|_| |_|____/|_|\___/|_| |_|___/
""",
        r"""
   __  __       _              ____              _
  |  \/  |     (_)            |  _ \            | |
  | \  / | __ _ _ _ __   ___  | |_) | ___   ___ | |_
  | |\/| |/ _` | | '_ \ / _ \ |  _ < / _ \ / _ \| __|
  | |  | | (_| | | | | |  __/ | |_) | (_) | (_) | |_
  |_|  |_|\__,_|_|_| |_|\___| |____/ \___/ \___/ \__|
"""
    ]

    intro = [
        r"=== \   |   /   ===",
        "===  - CHAOS MODE -  ===",
        r"=== /   |   \   ===",
        "",
        "Welcome to the wild side of the Python Project.",
        "Hold on — this landing page may behave unexpectedly.",
        "",
    ]

    chaotic_print(intro, delay=0.12, jitter=0.08)
    print(random.choice(banners))
    print()

    blurbs = [
        "✨ Anything can happen here.",
        "🎲 Random phrases are likely.",
        "⚡ Unexpected text may follow.",
        "🌪️ Chaos is the new calm.",
        "👾 Did you expect this? Probably not.",
    ]

    for line in random.sample(blurbs, k=3):
        print(line)
        time.sleep(0.12)

    print()
    print("What this app does:")
    print(" - Prints a chaotic welcome experience")
    print(" - Surprises you with unexpected output")
    print(" - Continues to the normal greeting afterward")
    print()
    print(textwrap.fill(
        "This landing page is intentionally messy: random banners, jittery timing, "
        "and surprising text appear to keep the experience energetic.",
        width=72
    ))
    print()

    prompts = [
        "Press Enter to survive this landing page...",
        "Push Enter and see what happens next...",
        "Continue, if you dare...",
        "Enter the next step by pressing Enter...",
    ]

    input(random.choice(prompts) + "\n")
    print()


def main() -> None:
    show_landing_page()
    print("Hello, World! The chaos has stabilized.")


if __name__ == "__main__":
    main()
