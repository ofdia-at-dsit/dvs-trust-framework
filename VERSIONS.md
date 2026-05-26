> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published policy, see the [UK digital verification services trust framework 1.0 on GOV.UK](https://www.gov.uk/government/publications/uk-digital-verification-services-trust-framework-1-0/uk-digital-verification-services-trust-framework-1-0-pre-release).

# Versions

The UK digital verification services trust framework is revised iteratively. This repository is designed to host multiple versions side by side, each in its own top-level folder named `trust-framework-<major>.<minor>/`, so that readers can always reach a specific published version through a stable URL.

## Currently hosted versions

| Version | Status | Folder | Certification notes |
| --- | --- | --- | --- |
| 1.0 | Current | [`trust-framework-1.0/`](trust-framework-1.0/README.md) | See [`trust-framework-1.0/00-version-and-certification-validity-notes.md`](trust-framework-1.0/00-version-and-certification-validity-notes.md) |

Earlier published versions of the framework (for example the gamma (0.4) publication and the beta (0.3) publication) are not hosted in this repository at launch. They can be added later in the same pattern if there is demand — a `trust-framework-0.4/` folder following the same internal layout.

## Adding a new version

When a new publication version (for example 1.1 or 2.0) is released on GOV.UK:

1. Create a new sibling folder `trust-framework-<major>.<minor>/`.
2. Inside it, replicate the Part 1–4 structure used in [`trust-framework-1.0/`](trust-framework-1.0/README.md), with one Markdown file per main numbered section.
3. Add the standard caution block to every file.
4. Populate each file with the publication text exactly as published.
5. Add a version README at `trust-framework-<major>.<minor>/README.md` following the same pattern as the 1.0 version README.
6. Add a new row to the "Currently hosted versions" table above.
7. Record the addition in [`CHANGELOG.md`](CHANGELOG.md) with a `[repo]` entry.
8. If the new version supersedes an earlier one for new certifications, update the "Status" column of both rows in the table above.

## Relationship to supplementary codes

Supplementary codes (for example for digital right to work, right to rent, or Disclosure and Barring Service identity checks) have their own version cycles and live in a separate [`supplementary-codes/`](supplementary-codes/README.md) folder when added.

## Back

- [Repository home](README.md)
