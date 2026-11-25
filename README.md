# MOBGAME

A handheld game console in a single HTML page — a little space, a big adventure.

The console sits in the middle of the screen and scales to fit any window, from desktop to phone. The design comes from the Figma file *Handheld – Game Console*.

## Games

The handheld starts on a menu with the dot-matrix MOBGAME logo. Pick a game with ↑ ↓ and press A or Start; press B to go back to the menu.

- **Star Drifter** — a little space, a big adventure
- **Brick** — break them all

More games will follow.

## Controls

| Key | Button |
| --- | --- |
| ↑ ↓ ← → | D-pad (move) |
| Space | A (shoot) |
| X | B (dash) |
| Enter | Start |

The buttons can also be clicked or tapped. **SOUND OFF / ON** toggles short 8-bit beeps.

## Run it

Open `index.html` in a browser. It is fully self-contained, so no server or build step is needed.

## Edit it

- `src/template.html` — the source of the page (HTML, CSS and JavaScript)
- `src/assets/` — the screen scene and the A/B button texture
- `src/build.py` — inlines the images and writes `index.html`

After changing the template, rebuild with:

```bash
python3 src/build.py
```

## Roadmap

- Make *Star Drifter* playable: movement, shooting, enemies, score and lives
- Make *Brick* playable: paddle, ball, bricks, score and levels

© BEARDY-NL
