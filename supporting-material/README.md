> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published policy, see the [UK digital verification services trust framework 1.0 on GOV.UK](https://www.gov.uk/government/publications/uk-digital-verification-services-trust-framework-1-0/uk-digital-verification-services-trust-framework-1-0-pre-release).

# Supporting material

This folder holds diagrams, examples, mappings, annexes, derived artefacts and other implementation aids that sit **alongside** the UK digital verification services trust framework but that are **not** part of the official Trust Framework publication text.

Everything in this folder is either derived from the publication (and clearly marked as derived) or added by repository maintainers and contributors to help readers apply the framework in practice. For the authoritative publication text, see the [`trust-framework-1.0`](../trust-framework-1.0/README.md) folder or the publication on GOV.UK.

## Contents

### Glossary (derived)
A machine-readable mirror of the section 16 glossary and abbreviations, for use by tooling (link checkers, auto-glossary tooltips, search indexes, etc.). See [`glossary.yaml`](glossary.yaml).

If the YAML and the publication text disagree, the publication is authoritative. Regenerate by running [`scripts/generate_glossary.py`](scripts/generate_glossary.py).

### Scripts
Helper scripts maintained alongside supporting material. See [`scripts/`](scripts/).

## Accessibility

Basic accessibility for the publication's figures is provided by alt text on the Markdown image references in the section files themselves. A separate folder of longer-form text descriptions has not been added. If someone does a dedicated accessibility pass, a `figure-descriptions/` folder or similar can be added back here with richer descriptions without affecting the rest of the repository.

## Proposing new supporting material

Use the [supporting material proposal issue template](../.github/ISSUE_TEMPLATE/07-supporting-material.yml) or open a pull request directly. See [`CONTRIBUTING.md`](../CONTRIBUTING.md) for the contribution process.

Typical future contents might include:

- explanatory diagrams of roles, relationships and flows
- worked examples and reference scenarios
- cross-mappings between trust framework sections and external standards
- annexes, checklists and implementation notes

## Back

- [Repository home](../README.md)
