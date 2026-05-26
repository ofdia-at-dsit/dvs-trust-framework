> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published policy, see the [UK digital verification services trust framework 1.0 on GOV.UK](https://www.gov.uk/government/publications/uk-digital-verification-services-trust-framework-1-0/uk-digital-verification-services-trust-framework-1-0-pre-release).

# Known issues

Items that have already been identified by maintainers but are not yet fixed. Each one will be migrated to a GitHub issue on first public push, and this file will wind down as issues move to proper tracking.

Each item names the category it would be raised under and a severity in the maintainer's view.

## Open

### KI-9 — Deliberate typographic NBSPs in ISO/IEC references were removed

**Category:** typo-or-correction
**Severity:** very low

**Files affected:**
- [`trust-framework-1.0/part-3/12-service-requirements.md`](trust-framework-1.0/part-3/12-service-requirements.md) — lines around the ISO/IEC 10118, 18031, 18032 and 18370 references
- [`trust-framework-1.0/part-4/15-table-of-standards-guidance-and-legislation.md`](trust-framework-1.0/part-4/15-table-of-standards-guidance-and-legislation.md) — the standards table rows with ISO/IEC references

**What is wrong:** The publication source originally used non-breaking spaces (U+00A0) between `ISO/IEC` and its numeric identifier (for example `ISO/IEC` + NBSP + `18370`) so the standard name would not be split across a line break when rendered on GOV.UK. When the broader NBSP cleanup ran (see resolved KI-3 below), these deliberate typographic NBSPs were converted to regular spaces along with the cosmetic ones.

**Impact:** No functional impact. Links still resolve, text reads correctly, and on GitHub the difference is invisible because GitHub's Markdown renderer treats both characters identically in line-wrapping. The only place the change is visible is a GOV.UK-style rendering, where an ISO/IEC reference might now split across a line break.

**Suggested fix:** an editor restores `\u00a0` between `ISO/IEC` and the number in the affected lines before the repository is used as a re-publication source for GOV.UK. Low priority because the cosmetic typography only matters on GOV.UK's rendering pipeline and can be re-applied by OfDIA editors at that stage.

## Owner: user

### KI-6 — CODEOWNERS handles are placeholders

**Category:** structural-feedback
**Severity:** blocker for public push
**Status:** **User will apply the fix upstream before public push.**

**Files affected:** [`.github/CODEOWNERS`](.github/CODEOWNERS), and `.github/ISSUE_TEMPLATE/config.yml` which references `OWNER/REPO` in links.

**What is wrong:** Team handles `@ofdia-maintainers`, `@ofdia-policy`, `@ofdia-engineering` and the string `OWNER/REPO` are placeholders that need to be replaced with the real GitHub organisation and team handles before the repository is used publicly, otherwise review routing will silently fail.

## Resolved (during pre-publication setup)

These items were raised earlier and are now addressed. They are retained here briefly for traceability; the summary log of how they were fixed is in [`CHANGELOG.md`](CHANGELOG.md) under "Pre-publication setup".

- **KI-1** — `<sup>Figure N<sup>` rendered incorrectly. *Resolved.* All four figure captions now use a proper closing `</sup>`. As part of the same pass, the GOV.UK-style `[Image: XXX.svg]` references were converted to standard Markdown image syntax with alt text so the figures actually render on GitHub.
- **KI-2** — Kramdown `{:#section-N}` anchors do not resolve on GitHub. *Resolved.* Anchors converted to invisible HTML anchors; cross-file fragment references rewritten to point at the correct target files. Same-file fragment links now work on GitHub.
- **KI-3** — Non-breaking spaces in headings and scattered body text. *Resolved*, with a narrower follow-up now tracked as KI-9. The cleanup removed all 268 NBSPs from the publication files rather than the 35 in headings that were originally in scope.
- **KI-4** — Image placeholders are empty. *Resolved.* Real SVG files for Figures 2, 3 and 4 are now in `/media/`.
- **KI-5** — Figure descriptions were placeholder drafts. *Resolved.* The `supporting-material/figure-descriptions/` folder has been removed; basic accessibility is now provided by alt text on the Markdown image references in the section files themselves. A deeper accessibility pass could add richer text descriptions in future without affecting the rest of the repository.
- **KI-7** — Licence specifics to confirm. *Resolved.* `LICENCE.md` updated to follow the [GDS Way licensing manual](https://gds-way.digital.cabinet-office.gov.uk/manuals/licensing.html): OGL v3.0 for documentation, the full MIT License text for code, and the correct Crown Copyright line. Maintainers should still confirm with DSIT/OfDIA that GDS Way's convention is a fit, because GDS Way is scoped to the GDS Product Group rather than DSIT.
- **KI-8** — `$CTA` markers render as literal text on GitHub. *Resolved.* All `$CTA … $CTA` pairs replaced with standard Markdown blockquotes around the illustrative-example content.
- **KI-10** — Rendered site's `govuk-frontend` CSS referenced assets at absolute paths that break on GitHub Pages subpath deploys. *Resolved.* The Eleventy config now reads the vendored CSS at build time, rewrites `url(/assets/...)` references using a `BASEURL` environment variable, and writes the adjusted file to `_site/stylesheets/`. The CI workflow passes `steps.pages.outputs.base_path` into the build as `BASEURL`, so the site works whether deployed at a domain root (BASEURL empty) or a repo subpath such as `https://user.github.io/dvs-trust-framework/`.

## How to raise new items

New items identified after first public push should go directly into GitHub issues using the templates in [`.github/ISSUE_TEMPLATE/`](.github/ISSUE_TEMPLATE/). This file exists only to seed the initial backlog.

## Back

- [Repository home](README.md)
