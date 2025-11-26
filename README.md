# Fishing Friday

Fishing Friday is a cozy 2D pixel art fishing adventure built around the ritual of logging in every Friday to discover fresh surprises. The game blends nostalgic Game Boy Advance palettes with modern high-fidelity pixel shading, pairing chunky pixels and smooth sub-pixel animation to create a warm, living world.

## Visual Style
- **Pixel-rich environments:** Layered parallax backgrounds, soft warm lighting, and gentle sunrise glows across every biome.
- **Lively details:** Environmental particles like drifting leaves, pollen, and fireflies; 2-layer transparency on shimmering water; fog layers and rippling caustics that react to footsteps and cast direction.
- **Handcrafted mood:** Soft pastel skies and cozy color grading with a balance of nostalgic simplicity and highly detailed spritework.

## Biomes
- Quiet forest ponds framed by tall reeds and cattails.
- Fast rivers cutting through mossy rock cliffs.
- Vast oceans with rolling waves and pixelated sunlight streaks.
- Hidden swamp groves filled with lilypads and neon amphibians.
- Deep cave lakes lit by bioluminescent fish beneath crystal stalactites.
- Surreal Friday-only dream biomes with inverted colors, shifted gravity, sky-swimming legends, and phase-shifting waters.

## Fish & Animation
- **Over 1000 catchable species** with distinct outlines, motion loops, and micro-animations (scale shimmer, fin flutter, glowing eyes for magical types).
- Expressive behaviors and color shifts that make every catch feel unique.

## Fishing Mechanics
- Simple to learn, deep to master: timing, tension control, rod perks, fish behavior, and environmental conditions.
- Satisfying casting loop with stretchy line sprites, bending rods, and chunky splash bursts.

## Rod Collection
- **50+ unique rods** with illustrated silhouettes: wooden poles, ornate elven rods, neon cyberpunk rigs, volcanic crystal rods, antique rusted poles, joke rods (umbrellas, broomsticks), and ultra-rare mythical rods forged from dreamstone, stardust, or legendary scales.
- Abilities include extended cast distance, faster reel speed, tension forgiveness, auto-lure movement, double catch chances, weather affinity, and time-shifted bites synced to Friday cycles.

## Friday Cycle
- Every real-world Friday unlocks temporary world changes: color shifts, NPC dialogue, shop discounts, migrating fish waves, mythic spawns, anomalies like glittering whirlpools or sky portals.
- Special Friday chiptunes distort and harmonize with the main theme, reinforcing the weekly ritual.

## NPCs & Lore
- Quirky, friendly characters with expressive pixel portraits (eyebrow shifts, blinking, subtle animations).
- Micro-quests tied to favorite fish or Friday traditions, plus cozy lore about ancient legends, lost underwater civilizations, and the metaphysics of Friday anomalies.

## UI & Audio
- Minimalist rounded UI inspired by classic GBA RPG menus, modernized with soft shadows and warm palettes.
- Consistent 12×12 or 16×16 pixel icons for fish, rods, bait, and upgrades.
- Hybrid chiptune + soft synth soundtrack with acoustic plucks, airy pads, and lo-fi percussion that shifts with weather, time, and biome: storms add muted drums and wind; mornings bring marimba-like chimes; nights feature bells and echoing droplets.

## Mood & Goals
Fishing Friday aims to be peaceful, hypnotic, and deeply collectible—a cozy ritual players revisit weekly to unwind, complete their catalog, uncover secrets, and chase rare Friday-only discoveries.

---

## Play the text prototype

A cozy text-first prototype is included so you can practice the weekly ritual right in the terminal.

### Requirements
- Python 3.10+

### Run interactively
```
python -m fishing_friday
```
Use the prompts to travel, cast, swap rods, and view your caught fish.

### Auto-play showcase
```
python -m fishing_friday --auto-play 3 --day Friday --seed 7
```
Runs three quick casts with Friday bonuses and a deterministic seed so you can see the loop without manual input.
