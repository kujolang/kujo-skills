# Skill Launch Variant

- Create or update skills with Skill Creator conventions: concise `SKILL.md`, specific trigger description, imperative instructions, one-level references, deterministic scripts only when useful, and matching `agents/openai.yaml`.
- Validate every new skill independently with `quick_validate.py`, then run the skills distribution's complete inventory, routing, link, clean-install, and release gates.
- Update the canonical skill index, expected routing map, positive/negative trigger fixtures, inventory counts, package version, changelog, spec/eval version, and README.
- Preserve the boundary that skills provide instructions and resources; the host remains responsible for runtime enforcement and permissions.
- Publish the skills-pack release before synchronizing website skill pages. Derive each page from the released `SKILL.md` and keep operational trigger detail concise on catalog cards.
- Generate a unique dither hero and dependent social card for every new public skill route.
