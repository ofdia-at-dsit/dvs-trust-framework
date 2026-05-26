> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published policy, see the [UK digital verification services trust framework 1.0 on GOV.UK](https://www.gov.uk/government/publications/uk-digital-verification-services-trust-framework-1-0/uk-digital-verification-services-trust-framework-1-0-pre-release).

# Changelog

This changelog records notable changes to this repository and to the publication text it hosts.

During the **pre-publication phase** (before 1.0 is formally published on GOV.UK), structural and formatting churn on the Markdown files is expected and is recorded here only at a summary level. Once 1.0 is formally published, this changelog moves to per-change tracking distinguishing repository changes (`[repo]`) from publication changes (`[publication]`).

The format loosely follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Once public, the repository follows [Semantic Versioning](https://semver.org/) for its own release tags, independent of the trust framework publication version.

---

## [Unreleased]

### Pre-publication setup

Initial scaffold of the repository around the UK digital verification services trust framework 1.0 publication:

- Publication text split into one Markdown file per main numbered section under `trust-framework-1.0/`, organised into Parts 1–4.
- Standard caution block on every Markdown file.
- README landing pages for the repository, for each version, for each Part, and for the media, supporting-material, additional-information and supplementary-codes folders.
- Previous / part / version / home / next navigation footers on every section file.
- Licence (OGL v3.0 for content, MIT for code), `CONTRIBUTING.md`, `SECURITY.md`, `CODEOWNERS`, `.editorconfig`, `.gitattributes`, `.gitignore`.
- Issue templates covering typo / clarity / structural / accessibility / broken-link / policy-feedback / supporting-material contribution routes, plus a pull-request template.
- CI workflows: caution-block integrity check, Markdown lint (relaxed), weekly external link check.
- Machine-readable glossary derived from section 16 (`supporting-material/glossary.yaml`), regenerable via script.
- Placeholder figure descriptions for Figures 2, 3 and 4 (Figure 1 is a table, not an image).
- `VERSIONS.md`, `ARCHITECTURE.md`, `KNOWN-ISSUES.md`.

Formatting cleanups applied across `trust-framework-1.0/` to make the files render properly on GitHub while preserving all visible narrative text:

- Kramdown attribute-list anchors (`{:#section-N}`) → invisible HTML anchors (`<a id="section-N"></a>`).
- Cross-file fragment references (`[text](#section-N)`) → explicit relative links to the target file and anchor (`[text](../part-X/NN-file.md#section-N)`).
- `$CTA … $CTA` delimiter pairs around illustrative examples → standard Markdown blockquotes.
- 268 U+00A0 non-breaking spaces replaced with regular spaces across 14 files (grep / copy-paste ergonomics; no visible change to rendering).

Each cleanup is driven by a reproducible script in `supporting-material/scripts/`.

Real SVG files added to `/media/` for Figures 2, 3 and 4, replacing the launch-time placeholders.

Non-breaking spaces (U+00A0) in the publication files converted to regular spaces (U+0020). Originally scoped to headings only, the cleanup turned out to be broader and removed all 268 NBSPs across the publication files. Any deliberate typographic NBSPs — for example those keeping `ISO/IEC` with a standard number on one line — will need to be re-applied by an editor before the repository is used as a re-publication source. Tracked as KI-9.

`LICENCE.md` aligned with the [GDS Way licensing manual](https://gds-way.digital.cabinet-office.gov.uk/manuals/licensing.html): the full MIT License text for code and Open Government Licence v3.0 for documentation, with a Crown Copyright line in the format that GDS Way recommends.

Figure handling finalised:

- `<sup>Figure N<sup>` captions closed properly as `<sup>Figure N</sup>`.
- GOV.UK-style `[Image: XXX.svg]` references converted to standard Markdown image syntax with alt text, so the figures render on GitHub as well as GOV.UK.
- The `supporting-material/figure-descriptions/` folder of placeholder descriptions has been removed. Basic accessibility is handled via alt text on the image references; a future accessibility pass can add richer descriptions back as new supporting material if wanted.

Caution banner on every Markdown file updated to include a direct link to the authoritative 1.0 publication on GOV.UK. The CI workflow that enforces the caution block content has been updated to match. (The banner link text was later revised to drop the "pre-release" wording while the publication's GOV.UK URL — which still contains the `-pre-release` slug — was preserved.)

Top-level `README.md` rewritten so it describes the **repository** rather than paraphrasing the policy. The previous version duplicated publication content (sections 2, 13 and 14) and referenced specific blog posts that would go stale. The new version focuses on the GOV.UK link, navigation into the publication files, and pointers to the repo's own documentation. Empty banner image references were dropped; filenames remain reserved in `/media/`.

OfDIA banner image added at the top of the README (`media/ofdia-banner.png`).

GOV.UK-styled static site layer added under [`docs-site/`](docs-site/README.md). Built with Eleventy and the official `govuk-frontend` npm package, modelled on the OfDIA data-schema-docs repository for toolchain consistency. Publication source Markdown is unchanged — the site uses the repository root as its input directory and adds layouts, includes, a GOV.UK-publishing `govspeak.js` markdown-it plugin, a `.eleventyignore` at the repo root, and a GitHub Actions workflow that builds and deploys to GitHub Pages. The build reads a `BASEURL` environment variable (populated automatically by `actions/configure-pages` in CI) and rewrites `govuk-frontend`'s asset URLs so the site works on both root-domain and repository-subpath deploys.

[`LICENCE.md`](LICENCE.md) aligned with the [GDS Way guidance for open documentation repositories](https://gds-way.digital.cabinet-office.gov.uk/manuals/licensing.html): dual-licensed OGL v3.0 (documentation) + MIT License (code), with a proper "The MIT License" title and Crown Copyright / OfDIA attribution.

---

## [0.1.0] — First public snapshot (to be tagged at first public push)

Captures the state of the Unreleased section above. Post-launch changes will be tracked at the granularity described at the top of this file.
