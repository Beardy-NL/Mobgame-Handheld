# MOBGAME

A handheld game console in a single HTML page — a little space, a big adventure.

The console sits in the middle of the screen and scales to fit any window, from desktop to phone. The design comes from the Figma file *Handheld – Game Console*.

## Games

The handheld starts on a menu with the dot-matrix MOBGAME logo. Pick a game with ↑ ↓ and press A or Start.

**Star Drifter** — a vertical space shooter. Fly with the D-pad, shoot with A (hold for auto-fire) and dash sideways with B; a dash makes you briefly untouchable. Every 2,000 points takes you to a new sector, where enemies get faster and start firing back. You have 3 lives.

**Brick** — a falling-blocks puzzle. Move with ← →, turn with ↑ or A, soft-drop with ↓ and hard-drop with B. Full lines disappear; every 10 lines raises the level and the speed.

**3D Padel** — padel against the computer on a 3D court with glass walls. Move with the D-pad (↑ towards the net, ↓ back), press A for a drive and B for a lob. Hit the ball high and A becomes a smash. Hold ← or → while hitting to aim. The ball must bounce once on the other side before it may hit the glass; it is your point when it bounces twice there. Scoring is 0-15-30-40 with a golden point at 40-40, and the first to 3 games wins the match.

In every game, Start pauses. From the title, pause or game-over screen, B goes back to the menu. Best scores are kept in your browser.

## Controls

| Key | Button |
| --- | --- |
| ↑ ↓ ← → | D-pad |
| Space | A |
| X | B |
| Enter | Start |

The buttons can also be clicked or tapped. **SOUND OFF / ON** toggles the 8-bit sound effects.

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

- More games

© BEARDY-NL
