from __future__ import annotations

import datetime as _dt
import random
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

from .data import BIOMES, FISH, RODS, Biome, Fish, Rod, RARITY_WEIGHT


@dataclass
class Player:
    name: str = "You"
    coins: int = 18
    inventory: List[Fish] = field(default_factory=list)
    rod: Rod = field(default_factory=lambda: RODS[0])

    def add_catch(self, fish: Fish) -> None:
        self.inventory.append(fish)

    def total_value(self) -> int:
        return sum(fish.value for fish in self.inventory)


@dataclass
class GameState:
    player: Player
    biome: Biome = field(default_factory=lambda: BIOMES[0])
    day_override: Optional[str] = None
    rng: random.Random = field(default_factory=random.Random)


def is_friday(day_override: Optional[str] = None) -> bool:
    if day_override:
        return day_override.lower().startswith("fri")
    return _dt.datetime.now().weekday() == 4


def describe_day(day_override: Optional[str] = None) -> str:
    today = day_override.capitalize() if day_override else _dt.datetime.now().strftime("%A")
    marker = " (Friday bonuses active!)" if is_friday(day_override) else ""
    return f"Today is {today}{marker}"


def list_rods() -> List[Rod]:
    return RODS.copy()


def list_biomes() -> List[Biome]:
    return BIOMES.copy()


def list_fish_for_biome(biome: Biome) -> List[Fish]:
    return [fish for fish in FISH if fish.biome == biome.name]


def pick_random_fish(biome: Biome, rng: random.Random, friday: bool) -> Fish:
    fish_in_biome = list_fish_for_biome(biome)
    weights = []
    for fish in fish_in_biome:
        rarity_weight = RARITY_WEIGHT[fish.rarity]
        # Friday nudges rare fish forward
        if friday:
            rarity_weight *= 1.3 if fish.rarity in {"rare", "epic", "legendary"} else 1.05
        weights.append(rarity_weight)
    return rng.choices(fish_in_biome, weights=weights, k=1)[0]


def hook_success(biome: Biome, rod: Rod, rng: random.Random, friday: bool) -> bool:
    base = 0.45
    if friday:
        base += 0.1
    base += biome.hook_bonus + rod.hook_bonus
    return rng.random() < min(max(base, 0.15), 0.95)


def tension_summary(tension: float) -> str:
    filled = int(tension // 5)
    return f"[{('#' * filled).ljust(20)}] {int(tension)}%"


def fight_sequence(fish: Fish, rod: Rod, rng: random.Random, friday: bool) -> Tuple[bool, List[str]]:
    log: List[str] = []
    tension = 50.0
    forgiveness = 18 + rod.tension_forgiveness + (4 if friday else 0)

    for turn in range(1, 4):
        surge = rng.randint(-12, 12) + (fish.difficulty / 10)
        tension += surge
        log.append(f"The {fish.name} surges ({surge:+.1f} tension)! {tension_summary(tension)}")
        if tension <= 10 or tension >= 90:
            log.append("The line snapped! Too much tension.")
            return False, log

        choice = rng.choice(["reel", "hold", "slack"])
        if choice == "reel":
            tension += 12
            log.append("You reel firmly, pulling tension up.")
        elif choice == "slack":
            tension -= 10
            log.append("You ease the line and let the fish run.")
        else:
            log.append("You hold steady, letting the rod flex.")

        # Forgiveness reduces the swing back toward center
        toward_center = (50 - tension) * (forgiveness / 100)
        tension += toward_center
        log.append(f"The rod flex smooths things out. {tension_summary(tension)}")

        if tension <= 10 or tension >= 90:
            log.append("The line snapped! Too much tension.")
            return False, log

    log.append("You guide the catch into your net!")
    return True, log


def cast_line(state: GameState) -> Tuple[bool, Optional[Fish], List[str]]:
    friday = is_friday(state.day_override)
    log: List[str] = []

    if not hook_success(state.biome, state.player.rod, state.rng, friday):
        log.append("A bite nibbles then darts away. Try again!")
        return False, None, log

    fish = pick_random_fish(state.biome, state.rng, friday)
    log.append(f"Hooked a {fish.rarity} {fish.name}!")
    success, fight_log = fight_sequence(fish, state.player.rod, state.rng, friday)
    log.extend(fight_log)

    if success:
        state.player.add_catch(fish)
        payout = state.biome.base_payout + fish.value + (6 if friday else 0)
        state.player.coins += payout
        log.append(f"Earned {payout} shells. Total shells: {state.player.coins}")
        return True, fish, log

    return False, fish, log


__all__ = [
    "Player",
    "GameState",
    "is_friday",
    "describe_day",
    "list_rods",
    "list_biomes",
    "list_fish_for_biome",
    "cast_line",
]
