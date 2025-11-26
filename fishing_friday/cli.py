from __future__ import annotations

import argparse
import random
from typing import Optional

from .data import Biome
from .mechanics import (
    GameState,
    Player,
    cast_line,
    describe_day,
    is_friday,
    list_biomes,
    list_rods,
)


def prompt_choice(prompt: str, options: list[str]) -> str:
    while True:
        choice = input(prompt).strip().lower()
        if choice in options:
            return choice
        print(f"Choose one of: {', '.join(options)}")


def choose_biome(current: Biome) -> Biome:
    biomes = list_biomes()
    print("Where to fish next?")
    for idx, biome in enumerate(biomes, 1):
        marker = "(current)" if biome.name == current.name else ""
        print(f" {idx}. {biome.name} {marker}\n    {biome.description}")
    while True:
        try:
            pick = int(input("Select biome #: "))
            if 1 <= pick <= len(biomes):
                return biomes[pick - 1]
        except ValueError:
            pass
        print("Enter a valid number.")


def choose_rod(current_index: int) -> int:
    rods = list_rods()
    for idx, rod in enumerate(rods, 1):
        marker = "(equipped)" if idx - 1 == current_index else ""
        print(
            f" {idx}. {rod.name} {marker}\n    {rod.description} "
            f"(hook +{rod.hook_bonus:.0%}, forgiveness +{rod.tension_forgiveness})"
        )
    while True:
        try:
            pick = int(input("Select rod #: "))
            if 1 <= pick <= len(rods):
                return pick - 1
        except ValueError:
            pass
        print("Enter a valid number.")


def render_header(state: GameState) -> None:
    friday = is_friday(state.day_override)
    print("=" * 60)
    print("Fishing Friday - Cozy text edition")
    print(describe_day(state.day_override))
    print(
        f"Location: {state.biome.name} | Rod: {state.player.rod.name} | Shells: "
        f"{state.player.coins}"
    )
    friday_note = (
        "Shimmering anomalies drift across the water..." if friday else "Calm ripples wait for a bite."
    )
    print(friday_note)
    print("=" * 60)


def take_turn(state: GameState) -> bool:
    render_header(state)
    print("Actions: [c]ast | [t]ravel | [r]od | [i]nventory | [q]uit")
    action = prompt_choice("> ", ["c", "t", "r", "i", "q"])

    if action == "q":
        return False

    if action == "t":
        state.biome = choose_biome(state.biome)
        return True

    if action == "r":
        index = list_rods().index(state.player.rod)
        new_index = choose_rod(index)
        state.player.rod = list_rods()[new_index]
        print(f"Equipped {state.player.rod.name}\n")
        return True

    if action == "i":
        if not state.player.inventory:
            print("Your journal is empty. Time to fish!\n")
        else:
            print("Caught fish:")
            for fish in state.player.inventory:
                print(f" - {fish.name} ({fish.rarity}, worth {fish.value} shells)")
            print(f"Total catalog value: {state.player.total_value()} shells\n")
        return True

    success, fish, log = cast_line(state)
    for line in log:
        print(line)
    if success and fish:
        print(f"Added {fish.name} to your journal!\n")
    else:
        print("The fish got away...\n")
    return True


def run_auto_play(state: GameState, casts: int) -> None:
    print("Running cozy auto-play...\n")
    for _ in range(casts):
        success, fish, log = cast_line(state)
        for line in log:
            print(line)
        if success and fish:
            print(f"Catalogued {fish.name}. Shells now {state.player.coins}\n")
        else:
            print("That one slipped free.\n")

    print("Auto-play finished! Inventory summary:")
    for fish in state.player.inventory:
        print(f" - {fish.name} ({fish.rarity})")
    print(f"Total shells earned: {state.player.coins}")


def build_state(day_override: Optional[str], seed: Optional[int]) -> GameState:
    rng = random.Random(seed)
    return GameState(player=Player(), rng=rng, day_override=day_override)


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Fishing Friday - cozy text fishing adventure")
    parser.add_argument("--day", help="Override day of week (e.g. Friday) to activate bonuses")
    parser.add_argument("--seed", type=int, help="Random seed for reproducible runs")
    parser.add_argument("--auto-play", type=int, default=0, help="Run this many automatic casts then exit")
    args = parser.parse_args(argv)

    state = build_state(args.day, args.seed)

    if args.auto_play:
        run_auto_play(state, args.auto_play)
        return

    print("Welcome to Fishing Friday! Type the letter in brackets to act.")
    while take_turn(state):
        pass

    print("Thanks for visiting the water today! Happy Friday.")


if __name__ == "__main__":
    main()
