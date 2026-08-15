# Site Synchronization

## Source Of Truth

- Build public inventory from the released tag, release manifest, catalog, and canonical repository documentation.
- Preserve exact display names and canonical capitalization.
- Link to the correct organization, repository, release, and documentation routes.
- Keep public descriptive copy durable across patch releases. Pin versions only where reproducibility or compatibility requires it.

## Required Surfaces

Inspect and update every applicable surface as one dependency set:

- landing page, catalog, detail pages, team pages, and ecosystem overview;
- desktop and mobile navigation, filters, carousels, cross-links, and footer;
- item/team/workflow counts and any structured catalogs;
- hero or portrait source assets and optimized/generated derivatives;
- Howl or equivalent Open Graph/social images;
- titles, descriptions, canonicals, Open Graph/Twitter metadata, and structured data;
- sitemap, RSS/Atom feeds, robots policy, `llms.txt`, and other AI/search discovery files.

## Visual Dependency Order

1. Derive a distinct, grounded concept from each released artifact.
2. Generate and validate the final dither hero or agent portrait.
3. Integrate and visually inspect the asset at target dimensions and responsive breakpoints.
4. Generate dependent Howl/social assets.
5. Verify route-to-image uniqueness, dimensions, two-color/series constraints, alt text, captions, and social metadata.

Never accept a technically generated image that misses the established Kujo visual language.

## Verification

- Build from a clean source state.
- Validate generated output, internal links, schemas, metadata, image references, and discovery files.
- Run representative browser flows at desktop and mobile sizes.
- Run the scoped SEO/AI-search audit with immutable before evidence.
- After deployment, request every affected production route and inspect representative rendered output.
- Confirm the deployment commit and the site repository's final synchronization state.
