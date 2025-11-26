from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Rod:
    name: str
    description: str
    hook_bonus: float = 0.0
    tension_forgiveness: int = 0


@dataclass(frozen=True)
class Biome:
    name: str
    description: str
    hook_bonus: float = 0.0
    base_payout: int = 6


@dataclass(frozen=True)
class Fish:
    name: str
    biome: str
    rarity: str
    difficulty: int
    value: int


RODS: List[Rod] = [
    Rod(
        name="Willow Sprig",
        description="A flexible branch with twine. Forgiving for beginners.",
        hook_bonus=0.05,
        tension_forgiveness=12,
    ),
    Rod(
        name="Tidecaller's Reed",
        description="Tuned for river surges; steadies tension swings.",
        hook_bonus=0.08,
        tension_forgiveness=18,
    ),
    Rod(
        name="Lumen Glass Rod",
        description="Rare Friday rod that glows when legends stir.",
        hook_bonus=0.12,
        tension_forgiveness=22,
    ),
]

BIOMES: List[Biome] = [
    Biome(
        name="Forest Pond",
        description="Quiet water framed by reeds and cattails.",
        hook_bonus=0.05,
        base_payout=8,
    ),
    Biome(
        name="River Run",
        description="Mossy cliffs and fast current that pulls the line.",
        hook_bonus=0.03,
        base_payout=10,
    ),
    Biome(
        name="Open Ocean",
        description="Rolling waves and shimmering sunlight streaks.",
        hook_bonus=-0.02,
        base_payout=12,
    ),
    Biome(
        name="Dream Current",
        description="Friday-only current where gravity feels sideways.",
        hook_bonus=0.15,
        base_payout=16,
    ),
]

FISH: List[Fish] = [
    Fish("Reed Minnow", "Forest Pond", "common", difficulty=12, value=4),
    Fish("Golden Koi", "Forest Pond", "rare", difficulty=22, value=16),
    Fish("Crescent Catfish", "River Run", "uncommon", difficulty=18, value=10),
    Fish("Glass Trout", "River Run", "rare", difficulty=26, value=18),
    Fish("Sky Sailfish", "Open Ocean", "uncommon", difficulty=20, value=14),
    Fish("Sunrise Tuna", "Open Ocean", "rare", difficulty=28, value=22),
    Fish("Friday Wisp", "Dream Current", "epic", difficulty=30, value=30),
    Fish("Astral Ray", "Dream Current", "legendary", difficulty=34, value=45),
]

RARITY_WEIGHT = {
    "common": 0.55,
    "uncommon": 0.3,
    "rare": 0.12,
    "epic": 0.025,
    "legendary": 0.005,
}

RARITY_COLOR = {
    "common": "white",
    "uncommon": "cyan",
    "rare": "yellow",
    "epic": "magenta",
    "legendary": "bright_yellow",
}
