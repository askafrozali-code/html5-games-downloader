# Play6x

Play6x is a static HTML5 games hub built on top of this repository's game
list. It's a single-page style site: search and browse the full catalog of
games from `GAMES_LIST.txt`, and jump straight into a growing set of
**Play6x Originals** — real games you can play instantly, no download, no
build step.

## What's inside

- **`index.html`** — homepage: hero, live search, category/section tabs, and
  a responsive grid of every catalogued game.
- **`play.html`** — the game player page (`play.html?id=<game-id>`). Shows a
  playable game in an iframe, or a "coming soon" state with related titles
  for games that aren't wired up to real code yet.
- **`css/style.css`** — the Play6x dark/neon theme.
- **`js/games-data.js`** — the full game catalog (256 entries), generated
  from `GAMES_LIST.txt` plus a set of Play6x Originals. Each entry has
  `id`, `name`, `section` (`Main` / `Driving` / `Flash` / `Original`),
  `category`, `icon`, `playable`, and `path`.
- **`js/app.js`** / **`js/play.js`** — homepage and player page logic
  (search, filters, rendering).
- **`games/*.html`** — 14 self-contained, dependency-free HTML5 games:
  2048, Snake, Flappy Block, Pong, Brick Breaker, Memory Match,
  Tic Tac Toe, Connect Four, Minesweeper, Simon Says, Space Defender,
  Whack-a-Mole, Tetris, and Pacman.

## Why not all 256 games are playable

`GAMES_LIST.txt` and the downloader scripts in this repo catalog game
*names*, not shippable source code — most of the referenced repositories
are placeholders rather than real, working game projects. Rather than
linking to games that don't actually exist, Play6x:

1. Shows the **entire** list as a browsable, searchable catalog (all 256
   titles, organized by their original Main / Driving / Flash sections and
   sub-categories).
2. Ships 14 fully working, original HTML5 games built directly into the
   site so there's always something real to play.
3. Marks everything else "Coming Soon" on its game page, with suggestions
   for similar playable titles.

As real, working game builds become available, add them to
`js/games-data.js` (set `playable: true` and `path: "games/<file>.html"`)
or drop a new file into `games/` and reference it the same way.

## Running locally

No build step — just serve the folder statically:

```bash
cd play6x
python3 -m http.server 8000
# open http://localhost:8000
```

Or open `index.html` directly in a browser (some browsers restrict
`fetch`/module features under `file://`, but this site uses plain scripts
so it works fine either way).

## Deploying

Since it's fully static, `play6x/` can be published as-is to GitHub Pages,
Netlify, Vercel, or any static host — just set the site root to this
folder.
