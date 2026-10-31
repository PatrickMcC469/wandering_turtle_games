# Wandering Turtle Games — Studio Website

The website for Wandering Turtle Games, my independent game studio in Boise, Idaho, at **[wanderingturtlegames.com](https://wanderingturtlegames.com)**. It's a single-page hub where players can see the studio's games, watch the trailers, and click through to the app stores.

## Highlights

- **No frameworks:** Hand-written HTML and CSS, no JavaScript, and no build step. The first load is about 170 KB.
- **Mobile-first and accessible:** The layout was designed at phone width first. Every text and background color pair is checked against WCAG contrast standards with a small script ([`docs/contrast.py`](docs/contrast.py)) instead of judged by eye.
- **Fast media:** Logos are served as WebP with PNG fallbacks, and trailers use poster images so the video loads only when someone plays it.
- **Automated deployment:** Pushing to `main` runs a GitHub Actions workflow that publishes `site/` to GitHub Pages on the custom domain.

## Games featured

| Game | Status |
|---|---|
| [DinoLife: Prehistoric Survival](https://apps.apple.com/us/app/dinolife-prehistoric-survival/id6783614616) | Released (iOS) |
| [Adventurer's Vault](https://apps.apple.com/us/app/adventurers-vault/id6778613726) | Released (iOS and Android) |
| Tactical Tides | In development |
| Bug Game (working title) | In development |

## How it was built

The site was planned in stages: discovery, content, design, and then the build. Each decision and the reasoning behind it is recorded in the docs:

- [`docs/decisions.md`](docs/decisions.md): every decision and why it was made
- [`docs/design-brief.md`](docs/design-brief.md): visual direction and constraints
- [`docs/content.md`](docs/content.md): the page copy, written and approved before any styling
- [`docs/contrast.py`](docs/contrast.py): WCAG contrast checker for the color palette

## Run it locally

```bash
python -m http.server 8081 --directory site
```

Then open http://localhost:8081.
