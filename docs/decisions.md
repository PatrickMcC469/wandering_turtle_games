# Decision log

Record decisions here as they're made, with the reasoning. Future-you will thank present-you.

| Date | Decision | Why |
|---|---|---|
| 2026-09-21 | Discovery before code, same process as the soccer project | It worked. Six questions up front settled the site's purpose in one conversation instead of three rebuilds. |
| 2026-09-21 | **The site is a hub, not a pitch.** Purpose: one link Patrick can hand people where they discover the games and click through to get or support them. | Patrick: no socials yet, not hiring, not ready to bring people on. The page should do the one job that's real today. |
| 2026-09-21 | **Games first, community work second, contact last.** Hierarchy of the page. | WTG is a game studio that does community/web work because it cares about kids playing outside as much as playing games — and because it funds the studio. The soccer site is evidence of the mission, not a separate business. |
| 2026-09-21 | Primary action is "click through to a game," not "email me." Contact is footer-only. | The visitor Patrick has in mind is someone who wants to find his work. Clients who want to email will find the footer. |
| 2026-09-21 | **One page.** | Patrick: "one great page over five thin ones." Two released games, two in progress, one community project — that fits on one screen-height-and-a-half. |
| 2026-09-21 | Finished games get a card with screenshot + store badges. In-progress games get a visibly different "in the workshop" treatment with a one-liner and **no fake link**. | A card with no image is worse than no card; a button that goes nowhere breaks trust. Teaser images will replace the placeholder treatment when Patrick shares them. |
| 2026-09-21 | Adventurers Vault has App Store **and** Google Play; DinoLife is App Store only. Store links are a row of badges per card, not one button. | Patrick. Design the card for 1–n links from the start. |
| 2026-09-21 | Owyhee Outlaws is named on the page as community work, linked once it's live (~Dec 1). Section exists at launch with the link hidden. | It's the clearest example of the mission. Hiding the link rather than the section means launch day is a one-line change. |
| 2026-09-21 | Stack: plain HTML/CSS/JS, no frameworks, no build tools, no Node. | Patrick wants to understand every line. Nothing to install, nothing to pay for. Same as the soccer project. |
| 2026-09-21 | Host on **GitHub Pages**, public repo `PatrickMcC469/wandering_turtle_games`, deployed by a GitHub Actions workflow that uploads `site/` unchanged. | Free. Public because a static marketing site has nothing to hide (see later entry re: Pro). Actions instead of "deploy from branch" so the served folder can be `site/` and the docs stay out of the published site. |
| 2026-09-21 | Domain at Squarespace; email is Google Workspace. **DNS plan: add GitHub's four A records + a `www` CNAME; never touch MX, SPF/DKIM TXT, or Google verification records.** Patrick does the clicking. | Breaking email to launch a website is the classic mistake. Written steps go in `docs/launch.md` before anyone opens the DNS panel. |
| 2026-09-21 | Palette is **sampled from the logo** (navy ground, sage/mint greens, strap brown as a warm accent) and every text/background pair is **measured against WCAG AA** with a script before it ships. Numbers get logged here. | Patrick: "check contrast numerically, don't eyeball it." The soccer project caught two failing pairs this way. |
| 2026-09-21 | Tone: **cozy, handmade indie studio — but tidy.** Warm like the turtle; clean alignment and real typography so a soccer-league board member still trusts it. | Patrick chose cozy. "Tidy" is the guardrail that keeps it from reading as amateur. |
| 2026-09-21 | No Inter/Roboto/Arial/system-ui, no purple gradients, real texture (CSS grain, not a heavy image). Font candidates shown as rendered samples before choosing. | Patrick's constraints. Texture done in CSS so it costs bytes, not kilobytes. |
| 2026-09-21 | Fonts: **self-hosted woff2 in the repo.** | Self-hosted = no third-party request, works offline, site is fully in the repo. Cost is a few files (~100 KB). Google Fonts is fine too; the soccer site uses it. |
| 2026-09-21 | Game screenshots come from Patrick's own App Store listings. | He owns them. Faster than waiting for originals that live on another machine; originals can replace them later. |
| 2026-09-21 | Logo shipped as a resized WebP (~400 px and ~800 px) with PNG fallback, not the 1.2 MB original. | The original is 1240 px / 1.2 MB — most of a rural phone's patience. |
| 2026-09-21 | Local dev server on port **8081**. | Soccer project uses 8080; both may run at once. |
| 2026-09-21 | *Flag, not a decision:* App Store seller name is "Patrick McClain," not Wandering Turtle Games. | Normal for a solo dev; site says "by Wandering Turtle Games" regardless. Changeable in App Store Connect if an LLC is formed. |
| 2026-09-21 | Commits stay under the Boise State email for now (it carries GitHub Pro). Switch to the WTG address if the Pro benefits ever move. | Patrick. |
| 2026-09-21 | Repo is **public**, even though Pro would allow Pages on a private repo. | Nothing sensitive in a static marketing site; public repo doubles as a portfolio of how Patrick works (docs, decision log). Flip to private any time in repo settings without touching the site. |
