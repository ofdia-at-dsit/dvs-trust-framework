> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published policy, see the [UK digital verification services trust framework 1.0 on GOV.UK](https://www.gov.uk/government/publications/uk-digital-verification-services-trust-framework-1-0/uk-digital-verification-services-trust-framework-1-0-pre-release).

# Security policy

This repository is a workspace copy of the UK digital verification services trust framework and associated material. It is not a production system and does not process personal data, but we still want to hear about security issues that relate to it.

## What to report here

- Vulnerabilities in any CI workflow, script or tooling included in this repository.
- Content issues that could mislead readers in a security-sensitive way (for example, incorrect cryptographic guidance introduced by an edit).
- Supply-chain concerns with any dependency this repository pulls in.

## What to report elsewhere

- Vulnerabilities in a specific certified digital verification service should be reported to that service provider directly, and where appropriate to their Conformity Assessment Body (CAB) and to OfDIA.
- Vulnerabilities in GOV.UK, the register of digital identity and attribute services, or other government services are reported through those services’ own disclosure channels, not via this repository.

## How to report

Please **do not raise a public GitHub issue** for security matters.

Contact the repository maintainers listed in [`.github/CODEOWNERS`](.github/CODEOWNERS) via a private channel, or email the Office for Digital Identities and Attributes through the contact route listed on their [GOV.UK page](https://www.gov.uk/government/organisations/office-for-digital-identities-and-attributes).

We will acknowledge receipt, work with you on a reasonable disclosure timeline, and credit the reporter in any resulting advisory unless you prefer otherwise.

## Scope

In scope:

- This repository and its CI workflows.

Out of scope:

- Third-party services linked to from the repository.
- The authoritative GOV.UK publication (report via GOV.UK).
- Any downstream fork or mirror of this repository.
