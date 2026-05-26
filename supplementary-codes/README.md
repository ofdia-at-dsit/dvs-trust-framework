> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published policy, see the [UK digital verification services trust framework 1.0 on GOV.UK](https://www.gov.uk/government/publications/uk-digital-verification-services-trust-framework-1-0/uk-digital-verification-services-trust-framework-1-0-pre-release).

# Supplementary codes

This folder is reserved as the future home for **supplementary codes** to the UK digital verification services trust framework, hosted in the same Markdown-first, version-controlled format as the main framework.

Supplementary codes are explained in section 4.4 of the trust framework publication. In short, they are sets of additional certifiable rules that digital verification services can be certified against alongside the main trust framework, in order to meet the needs of a specific sector or use case (for example digital right to work checks, digital right to rent checks, or Disclosure and Barring Service identity checks).

The authoritative, current list of supplementary codes lives on GOV.UK:

- <https://www.gov.uk/government/collections/uk-digital-identity-and-attributes-supplementary-codes>

At the time of the 1.0 trust framework publication there are three published supplementary codes:

- Supplementary code for digital right to work checks
- Supplementary code for digital right to rent checks
- Supplementary code for Disclosure and Barring Service identity checks

## Proposed layout

When a supplementary code is added to this repository, it should follow the same pattern as [`trust-framework-1.0/`](../trust-framework-1.0/README.md):

```
supplementary-codes/
├── right-to-work-1.0/
│   ├── README.md
│   ├── <one Markdown file per main numbered section>
│   └── ...
├── right-to-rent-1.0/
│   └── ...
└── dbs-identity-checks-1.0/
    └── ...
```

Each supplementary code folder should:

- carry the standard caution block on every Markdown file
- follow the same Part / section pattern used for the main framework where the code has one
- link back to the version of the trust framework it sits alongside
- record its own version in [`../VERSIONS.md`](../VERSIONS.md) and its addition in [`../CHANGELOG.md`](../CHANGELOG.md)

## Not yet populated

At present this folder is intentionally empty other than a `.gitkeep` file. Proposals to add a supplementary code to the repository are welcome via the [supporting material issue template](../.github/ISSUE_TEMPLATE/07-supporting-material.yml) or a pull request — see [`CONTRIBUTING.md`](../CONTRIBUTING.md).

## Back

- [Repository home](../README.md)
