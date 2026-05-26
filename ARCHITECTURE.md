> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published policy, see the [UK digital verification services trust framework 1.0 on GOV.UK](https://www.gov.uk/government/publications/uk-digital-verification-services-trust-framework-1-0/uk-digital-verification-services-trust-framework-1-0-pre-release).

# Architecture

This document records the design decisions behind the repository so future maintainers can change them deliberately rather than accidentally.

## Goals

1. Make the UK digital verification services trust framework easier to **navigate, review, cite and reuse** as a set of Markdown files under version control.
2. Open a **structured route for feedback and contributions** from providers, regulators, researchers and the public.
3. Be unambiguous at all times that this is a **workspace copy** and that the authoritative publication lives on GOV.UK.
4. Work for **more than one version** of the framework, side by side, without churn.

## Key decisions

### One Markdown file per main numbered section

Each main numbered section of the publication (0, 1, 2, …, 16) is a standalone Markdown file. This is the granularity that maps to how the publication is cited and consulted, and is small enough to review in a single pull request.

Rejected alternatives:
- One file per Part (too large, diffs unwieldy).
- One file per subsection (fragmentation; cross-references harder to maintain; doesn't match how the publication is cited).

### Parts as folders

The four published Parts are reflected as folders under each versioned framework folder (`part-1/` … `part-4/`). This groups related sections and matches the publication's own structure.

### The caution block is the one content invariant

Every Markdown file in the repository begins with the same caution block:

```
> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published policy and Trust Framework materials, visit GOV.UK.
```

This is the repository's single mechanism for making the workspace-versus-publication distinction visible on every file anyone might land on. It is enforced by the [caution-block CI workflow](.github/workflows/caution-block.yml).

### The publication text is editable, but changes are tracked

During repository creation, the publication text was copied verbatim with no changes other than the caution block. After creation, the publication text is **open to proposed changes** through the standard contribution process described in [`CONTRIBUTING.md`](CONTRIBUTING.md). Changes that alter the meaning of a rule are escalated to the Office for Digital Identities and Attributes (OfDIA) rather than merged by maintainers alone, because a GitHub merge does not by itself change government policy.

Each change is classified in [`CHANGELOG.md`](CHANGELOG.md) as either `[repo]` (structural / tooling / navigation) or `[publication]` (text of a published version).

### Versions are sibling top-level folders

New publication versions are added as new sibling folders (`trust-framework-1.1/`, `trust-framework-2.0/` and so on). This keeps URLs stable for earlier versions and avoids reorganising the repository every time a new version is published. See [`VERSIONS.md`](VERSIONS.md).

### Supplementary codes live in their own top-level folder

Supplementary codes are separate publications with their own version cycles. They belong in [`supplementary-codes/`](supplementary-codes/README.md), not inside a trust-framework-version folder.

### Supporting material is clearly separated

Anything not part of an official publication — diagrams, figure descriptions, derived YAML, worked examples, mappings, scripts — lives in [`supporting-material/`](supporting-material/README.md). Derived artefacts are marked as derived and name the authoritative source.

### Images are placeholders at launch

The files in [`media/`](media/README.md) are empty placeholders with the exact filenames used by the publication and the top-level README. This wires up the Markdown links so that real images can be dropped in without any cross-reference churn.

### Kramdown anchors have been converted, and cross-file links rewritten

The publication source on GOV.UK uses Kramdown-style anchors (`{:#section-14}`, etc.) which GitHub's Markdown renderer ignores and prints as literal text. In this repository those anchors have been converted to invisible HTML anchors (`<a id="section-14"></a>`), and every cross-file fragment reference (`[section 14](#section-14)` in a file other than section 14's) has been rewritten to an explicit path (`[section 14](../part-3/14-the-uk-certifid-trust-mark.md#section-14)`).

The result on GitHub:

- no literal `{:#...}` artefacts remain visible anywhere
- same-file fragment links resolve via the HTML anchors
- cross-file fragment links resolve via the explicit file paths

The anchor IDs are preserved so the files can be round-tripped back to Kramdown if this repository ever becomes a publication source. The conversion is reproducible via scripts in [`supporting-material/scripts/`](supporting-material/scripts/).

### `$CTA` markers replaced with Markdown blockquotes

The publication source uses `$CTA … $CTA` delimiter pairs around illustrative-example blocks to tell the GOV.UK renderer to render them as call-to-action panels. GitHub has no equivalent and prints the markers as literal text. In this repository the markers have been replaced with standard Markdown blockquotes so each example appears as a visually distinct panel on GitHub without any change to the narrative text of the example.

### Navigation footers

Each section file ends with a repository navigation block (previous / part / version / home / next), separated from the publication text by a horizontal rule and a "Repository navigation" heading. The separation is deliberate and is always obvious to a reader.

### Contribution routing is template-driven

Seven issue templates capture the main categories of contribution and route them to the right reviewers via [`.github/CODEOWNERS`](.github/CODEOWNERS). The PR template has a structured self-checklist including the caution-block invariant and a flag for substantive policy changes.

## What this repository deliberately does not do

- It does not override or modify GOV.UK.
- It does not enforce immutability of the publication text after launch. The repository is a living workspace.
- It does not store personal data or production secrets.

## Rendered site layer

A GOV.UK-styled rendered view of the workspace lives under [`docs-site/`](docs-site/README.md). It is built with [Eleventy](https://www.11ty.dev/) and the official [govuk-frontend](https://github.com/alphagov/govuk-frontend) package, modelled on the pattern used by the OfDIA data-schema-docs site for toolchain consistency.

The rendered site is a **view**, not an authority. Three constraints follow:

- The Markdown source is not duplicated. Eleventy's input directory is the repository root; the site adds layouts, includes and data alongside it in `docs-site/` without touching any existing content.
- Cross-file `.md` links in publication content are rewritten to pretty URLs at output time, so the source files stay `.md`-linked (which is what GitHub's native Markdown rendering expects) while the rendered site links resolve without `.md` suffixes.
- The site understands the GOV.UK publishing "GovSpeak" block markup — `$CTA`, `$E`, `%…%` warnings, `^…^` help notices — via a `govspeak.js` markdown-it plugin. This preserves publishing parity with GOV.UK so source prose can stay close to what publishers would write.

The site does not change any of the invariants above. Publication text, caution banner, cross-file link targets, and the `trust-framework-<version>` folder structure all remain the authoritative layout. If the site tooling were removed tomorrow, the repository would still be a coherent workspace copy.

## Back

- [Repository home](README.md)
