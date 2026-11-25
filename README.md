# MOBGAME

A handheld game console in a single HTML page — a little space, a big adventure.

The console sits in the middle of the screen and scales to fit any window, from desktop to phone. The design comes from the Figma file *Handheld – Game Console*.

## Games

The handheld starts on a menu with the dot-matrix MOBGAME logo. Pick a game with ↑ ↓ and press A or Start.

**Tennis** — 1 vs 1 against the computer on a 3D tennis court. Move with the D-pad, A for a drive (a smash when the ball is high), B for a lob; hold ← or → while hitting to aim. The first bounce has to land inside the singles lines. Real tennis scoring with deuce and advantage; first to 3 games wins. After every point your player has something to say about it.

**Basketball** — score as many points as you can in 30 seconds. A power bar runs back and forth under the ball; press A (or B) when the marker is in the dark zone to shoot it in, and dead centre for a swish. Line the ball up under the hoop with ← →. After 5 baskets the hoop starts sliding from side to side. A basket is worth 2 points, a swish 3.

**Padel** — 2 vs 2 padel on a 3D court with glass walls: you and a computer partner against two computer players. You are the player with the ▼ marker; your partner covers the other half. Move with the D-pad (↑ towards the net, ↓ back), press A for a drive and B for a lob. Hit the ball high and A becomes a smash. Hold ← or → while hitting to aim. The ball must bounce once on the other side before it may hit the glass; it is your point when it bounces twice there. After every point one of your team speaks up in a speech bubble — a compliment (or a cheeky claim) when you win the point, a grumble when the opponents do. Scoring is 0-15-30-40 with a golden point at 40-40, and the first to 3 games wins the match.

In every game, Start pauses. From the title, pause or game-over screen, B goes back to the menu. Best scores are kept in your browser.

## Controls

| Key | Button |
| --- | --- |
| ↑ ↓ ← → | D-pad |
| Space | A |
| X | B |
| Enter | Start |

The buttons can also be clicked or tapped. **SOUND OFF / ON** toggles all sound: soft retro clicks on the D-pad, A, B and Start, plus 8-bit effects and jingles in every game. With SOUND OFF everything is silent.

## Run it

Open `index.html` in a browser. It is fully self-contained, so no server or build step is needed.

## Edit it

- `src/template.html` — the source of the page (HTML, CSS and JavaScript)
- `src/assets/` — the A/B button texture
- `src/build.py` — inlines the images and writes `index.html`

After changing the template, rebuild with:

```bash
python3 src/build.py
```

## Roadmap

- More games

© BEARDY-NL
