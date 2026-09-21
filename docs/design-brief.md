# Design brief — Wandering Turtle Games

*The "detailed prompt" for design work. Written 2026-09-21 after discovery. Feed this to any design step.*

## Who it's for

People Patrick hands the link to: someone he met at an event, a player who liked one of the games, a community organization wondering if he's real. Mostly on phones. They already have a reason to look; the page's job is to reward the click, not to persuade a stranger.

## What it has to do (in priority order)

1. Show the games — finished ones with a way to get them, in-progress ones as a tease
2. Say what the studio is and where it is, in a sentence
3. Show the community work (Owyhee Outlaws, once live)
4. Give an email address

## The one thing to remember

**A turtle with a bedroll.** The logo is a small, warm, slightly whimsical traveler — unhurried, going somewhere. The site should feel like something that traveler made at a campsite table: cozy, handmade, cared-for. *But tidy* — straight lines, generous spacing, real typography. Not slick, not corporate, not "indie game template #4." Not cluttered either.

## Aesthetic direction

**Tone:** Cozy indie studio. Warm, calm, a little playful. Confident without volume.

**Typography:** A rounded or softly-drawn display face for headings that has some personality (candidates to render and compare: *Fredoka*, *Baloo 2*, *Grandstander*, *Sniglet*, *Chewy* — or a friendly slab like *Zilla Slab* / *Bitter* if the rounded faces read too childish). Body in a humanist face that's clean at small sizes on phones (*Nunito*, *Source Sans 3*, *Atkinson Hyperlegible*, *Lora* for a warmer serif option). **Not** Inter/Roboto/Arial/system-ui. One display + one body. Self-hosted woff2 unless decided otherwise; 2 families, ≤4 weights.

**Color (to be sampled from the logo and measured):**
- Deep navy — page ground, the "night sky" the turtle sits in
- Sage / mint greens — turtle, accents, headings on dark
- Strap brown — warm accent, sparingly (rules, a badge, hover)
- Every text/background pair ≥ 4.5:1 (body) or ≥ 3:1 (large text), verified by script, numbers logged in `decisions.md`

**Texture:** Subtle SVG/CSS grain over the navy so it feels like paper or night sky, not a flat hex. A faint path/trail motif is allowed if it stays in the background. No stock photos, no gradients doing the work.

**Motion:** At most one gentle entrance on the hero. Off under `prefers-reduced-motion`. The turtle does not bounce.

**Layout:** Mobile first. Single column on phones; game cards go 2-up from ~640 px. 16 px side gutters minimum. No horizontal scroll, ever.

## What to avoid

- Template look: hero-with-gradient, three-icon feature row, testimonial carousel
- Purple gradients, neon, "gamer" aesthetics (dark + RGB glow)
- Buttons or badges that link nowhere
- More than one page until there's a reason
- Anything that makes the logo compete with a second illustration style
