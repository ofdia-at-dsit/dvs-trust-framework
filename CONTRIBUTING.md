> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published policy, see the [UK digital verification services trust framework 1.0 on GOV.UK](https://www.gov.uk/government/publications/uk-digital-verification-services-trust-framework-1-0/uk-digital-verification-services-trust-framework-1-0-pre-release).

# Contributing

This repository is a **workspace copy** of the UK digital verification services (DVS) trust framework. It exists to make the framework easier to navigate, review and version, and to open up a clearer, more structured route for **feedback, suggestions and proposed changes**.

Contributions from providers, regulators, researchers, assistive-technology users, policy specialists, plain-English reviewers and the wider public are welcome.

> The authoritative version of the trust framework remains the publication on GOV.UK. This repository does not override it. Changes accepted here do not automatically become government policy — material revisions to the framework follow the Office for Digital Identities and Attributes (OfDIA) publication and consultation processes.

## What you can contribute

We particularly welcome contributions in these categories:

- **Corrections** — typos, broken links, formatting artefacts, misplaced punctuation.
- **Clarity and plain English** — suggestions for rephrasing that make a requirement easier to understand without changing its meaning.
- **Structural and navigation improvements** — to READMEs, cross-links, tables of contents, folder structure.
- **Accessibility** — alt text, figure descriptions, heading structure, reading order, colour-contrast issues in any images.
- **Supporting material** — diagrams, worked examples, mappings to external standards, annexes, implementation notes. These go in `supporting-material/`.
- **Policy feedback** — substantive points about the rules themselves. These will be escalated to OfDIA rather than merged directly.
- **Tooling** — CI workflows, linting, link checking, converters, renderers.

If you are unsure which bucket your contribution falls into, raise an issue first and we will help you route it.

## How to contribute

### 1. Raise an issue

The fastest way to propose something is to [open an issue](../../issues/new/choose) using one of the templates:

- **Typo or correction**
- **Clarity improvement**
- **Structural or navigation feedback**
- **Accessibility issue**
- **Broken or out-of-date link**
- **Policy feedback** (escalated to OfDIA)
- **Supporting material proposal**

Issues can be conversational. You do not need to bring a fix.

### 2. Open a pull request

If you have a concrete change in mind, fork the repository, make your change on a feature branch, and open a pull request. The PR template walks you through the basics.

### 3. Start a discussion

For broader, open-ended conversations that are not tied to a specific change, use [GitHub Discussions](../../discussions) on this repository.

## Ground rules

- **Assume good faith** and treat other contributors with respect.
- **One change per PR where possible.** Bundled changes are harder to review and harder to escalate to OfDIA if policy feedback is involved.
- **Keep the caution block.** Every Markdown file in the repository starts with the standard caution block reminding readers this is a workspace copy. Do not remove it. A CI check enforces this.
- **Flag substantive policy changes.** If your PR changes the *meaning* of a published rule (rather than its wording, formatting, or links), say so clearly in the PR description. These PRs will typically be held open pending OfDIA review rather than merged directly.
- **Respect personal data and privacy** in issues and PRs. Do not include personal data in examples, screenshots or logs.

## Style and formatting

- Markdown, one main numbered section per file, as currently structured.
- Use UK English spelling.
- Prefer plain text and accessible Markdown tables over images where possible.
- Images live in `/media` using the existing filenames.
- Line endings are LF (enforced by `.gitattributes`).
- Trailing whitespace inside the publication text is sometimes significant; leave it alone unless your change is specifically to clean it up and you note that.

## How proposed changes are reviewed

1. A repository maintainer (see `.github/CODEOWNERS`) triages the issue or PR within a reasonable timeframe.
2. Editorial, structural, accessibility and tooling changes can be merged directly after review.
3. Substantive changes to the meaning of published rules are logged and passed to OfDIA. Merging of those PRs follows OfDIA’s process, not GitHub review alone.
4. Accepted changes are recorded in [`CHANGELOG.md`](CHANGELOG.md), tagged `[repo]` or `[publication]` depending on their nature.

## Security

If you believe you have found a security issue, please do not raise it as a public issue. See [`SECURITY.md`](SECURITY.md).

## Code of conduct

Contributors are expected to follow the [Contributor Covenant](https://www.contributor-covenant.org/) version 2.1 or later. A dedicated `CODE_OF_CONDUCT.md` may be added in a future revision.

## Licence

By contributing, you agree that your contribution will be licensed under the same terms as the repository. See [`LICENCE.md`](LICENCE.md).
