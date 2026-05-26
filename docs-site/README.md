# docs-site

The GOV.UK-styled static site for this repository. Built with [Eleventy (11ty)](https://www.11ty.dev/) and the official [govuk-frontend](https://github.com/alphagov/govuk-frontend) npm package, following the pattern used by the OfDIA data-schema-docs site for toolchain consistency.

> [!IMPORTANT]
> The rendered site is a **view** of the repository. It is not the authoritative publication. The authoritative version of the UK digital verification services trust framework lives on GOV.UK. See [`../LICENCE.md`](../LICENCE.md) and the repository [`../README.md`](../README.md) for context.

## Architecture

- The Markdown source lives at the repository root (`trust-framework-1.0/**`, top-level READMEs, `CONTRIBUTING.md` etc). This folder does not duplicate any of it.
- Eleventy's input directory is `..` (the repo root), with `.eleventyignore` excluding build tooling.
- Layouts, includes, data and the markdown-it `govspeak.js` plugin all live inside this folder.
- The site builds into `_site/` (git-ignored).

```
docs-site/
├── package.json              deps: eleventy, markdown-it, markdown-it-anchor, govuk-frontend
├── .eleventy.js              config (permalinks, md links rewrite, passthrough copies)
├── govspeak.js               markdown-it plugin: $CTA, $E, %…%, heading classes, table classes
├── _layouts/
│   ├── default.html          full GOV.UK page chrome
│   └── page.html             adds a one-quarter TOC sidebar when headings exist
├── _includes/
│   ├── skip-link.html
│   ├── govuk-header.html
│   ├── service-navigation.html
│   ├── phase-banner.html
│   ├── page-title.html
│   ├── page-footer.html      edit-on-GitHub + raise-an-issue links
│   └── govuk-footer.html
└── _data/
    ├── site.json             OfDIA title, caption, phase banner text, repo URL
    └── eleventyComputed.js   default layout + permalink scheme + title fallback
```

## Local development

```bash
cd docs-site
npm install
npm start       # eleventy --serve, watches the repo, hot-reloads
```

Open <http://localhost:8080/>.

To build once for inspection without the dev server:

```bash
npm run build   # outputs to docs-site/_site/
```

## Deployment

The workflow at [`../.github/workflows/build-docs-site.yml`](../.github/workflows/build-docs-site.yml) builds the site on pushes to `main` and deploys to GitHub Pages using GitHub's native `actions/deploy-pages` action.

Before first deploy, in the repository settings under **Pages**, set the source to **GitHub Actions**.

### Subpath deployments

`govuk-frontend`'s CSS references assets under `/assets/...` (an absolute path from the site root). Out of the box this works only for root-domain deployments (e.g. `dvs-trust-framework.ofdia.gov.uk`).

For subpath deployments (e.g. `username.github.io/dvs-trust-framework/`), the build reads a `BASEURL` environment variable and rewrites `url(/assets/...)` to `url(${BASEURL}/assets/...)` in the vendored CSS before writing it to `_site/stylesheets/`. The CI workflow sets `BASEURL` automatically from `actions/configure-pages`'s `base_path` output, so the site works on GitHub Pages without additional configuration.

For local development `BASEURL` defaults to an empty string — `npm start` serves the site from the root of `localhost:8080`, so no rewrite is needed.

## Permalink scheme

The computed permalink in [`_data/eleventyComputed.js`](_data/eleventyComputed.js) mirrors the repository layout:

| Source file | URL |
| --- | --- |
| `README.md` | `/` |
| `trust-framework-1.0/README.md` | `/trust-framework-1.0/` |
| `trust-framework-1.0/part-1/README.md` | `/trust-framework-1.0/part-1/` |
| `trust-framework-1.0/part-1/01-introduction.md` | `/trust-framework-1.0/part-1/01-introduction/` |
| `CONTRIBUTING.md` | `/CONTRIBUTING/` |

Cross-file `.md` links inside publication content are rewritten to these pretty URLs at output time by a transform in `.eleventy.js` — the source files keep their `.md`-style links so they still resolve correctly when browsed on github.com.

## GovSpeak support

[`govspeak.js`](govspeak.js) is a markdown-it plugin derived from the OfDIA data-schema-docs site. It understands a subset of the GOV.UK publishing system's block markup so that source prose can stay close to what OfDIA publishers would actually write:

- `$CTA … $CTA` — call-to-action box
- `$E … $E`, `$C … $C`, `$D … $D`, `$A … $A` — example, contact, download, address boxes
- `^ help text ^` — help notice
- `% warning text %` — GOV.UK warning text component

It also applies govuk-body to paragraphs, govuk-heading-l/m/s to headings, govuk-inset-text to blockquotes, govuk-table scaffolding classes to tables, and govuk-link to in-content links. H1 in source content is downshifted to H2 so the layout's page title can remain the single H1 on the page.

## GitHub Alerts

The publication and supporting files use GitHub Alert syntax (`> [!CAUTION]`, `> [!IMPORTANT]`) which renders natively on github.com but not in plain markdown-it. The Eleventy config strips the `[!TAG]` label line before rendering, leaving the remaining blockquote content to render with the `govuk-inset-text` class. The visual effect is an inset notice, which is appropriate for both the caution banner and the important notice.
