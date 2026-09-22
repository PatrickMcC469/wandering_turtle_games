# Wandering Turtle Games — Website

The studio's own site at **wanderingturtlegames.com**. A single-page hub where people can discover the games, click through to download or support them, and see the community work the studio does.

**Status:** Page built 2026-09-22 — hero, games (with the DinoLife trailer), community, footer. Mobile first, zero JS, 138 KB first load, all contrast measured. Next: enable GitHub Pages, point Squarespace DNS, launch.

## Project brief

| | |
|---|---|
| **Owner** | Patrick McClain — Wandering Turtle Games, Boise, Idaho |
| **Purpose** | One link to hand people: "here's what we've made, here's what we're making, here's where to get it." |
| **Primary action** | Click through to a game's store page. Contact email lives in the footer; no hiring, no newsletter, no socials (none exist yet). |
| **Audience** | Anyone Patrick sends the link to: players, people met at events, potential community clients like the soccer league. |
| **Scope** | One page. Games (finished + in progress), community work, contact. Add pages only when there's something to put on them. |
| **Tech** | Plain HTML/CSS/JS, no frameworks, no build tools. GitHub Pages with the custom domain. $0/month. |
| **Domain / email** | Domain registered at Squarespace. Email `tevin_mcclain@wanderingturtlegames.com` is Google Workspace — its DNS records must not be touched. |

## Games (as of 2026-09-21)

| Game | Status | Where |
|---|---|---|
| DinoLife: Prehistoric Survival | Released | [App Store](https://apps.apple.com/us/app/dinolife-prehistoric-survival/id6783614616) |
| Adventurers Vault | Released | [App Store](https://apps.apple.com/us/app/adventurers-vault/id6778613726), Google Play (link TBD) |
| Tactical Tides | In progress | nothing to link yet — teaser images to come |
| Bug game (working title) | In progress | nothing to link yet — teaser images to come |

Community work: the [Owyhee Outlaws](https://github.com/PatrickMcC469/owyhee-outlaws) youth soccer league site, live ~Dec 1 2026. Linked from this page once it's up.

## Documents

- [`docs/decisions.md`](docs/decisions.md) — log of decisions made and why
- [`docs/design-brief.md`](docs/design-brief.md) — aesthetic direction, constraints, what to avoid
- [`docs/content.md`](docs/content.md) — every word on the page, approved plain before styling
- [`docs/contrast.py`](docs/contrast.py) — WCAG contrast checker for the palette; re-run when a color changes
- [`docs/font-samples.html`](docs/font-samples.html) — five font pairings rendered on the real palette (loads Google Fonts for comparison only)
- `docs/launch.md` — *(later)* GitHub Pages + Squarespace DNS steps, and what to leave alone

## Running locally

Everything under `site/` is the website; there is nothing to compile.

```bash
C:/Users/tevin/anaconda3/python.exe -m http.server 8081 --directory site
```

Then open http://localhost:8081. (Port 8081 so it doesn't collide with the soccer project on 8080.)

## Deploying

Push to `main`. The GitHub Actions workflow in `.github/workflows/pages.yml` uploads `site/` to GitHub Pages as-is. `site/CNAME` tells Pages which domain the site answers to.

## Process

1. **Discovery** — what it's for, who it's for, what exists to show ✅ 2026-09-21
2. **Skeleton** — repo, docs, deploy workflow ✅ 2026-09-21
3. **Content** — write the words, approve them plain ✅ 2026-09-21
4. **Design** — palette from the logo, fonts, texture; contrast measured, not eyeballed ✅ 2026-09-21
5. **Build** — mobile viewport first ✅ 2026-09-22
6. **Launch** — Pages, DNS, HTTPS *(next)*
7. **Dec 1** — unhide the Owyhee Outlaws link
