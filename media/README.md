> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published policy, see the [UK digital verification services trust framework 1.0 on GOV.UK](https://www.gov.uk/government/publications/uk-digital-verification-services-trust-framework-1-0/uk-digital-verification-services-trust-framework-1-0-pre-release).

# Media

This folder holds the images referenced from the publication files in this repository, plus a set of reserved filenames for future top-level banner illustrations.

## In use

- `ofdia-banner.png` — Office for Digital Identities and Attributes banner, used at the top of the repository README.
  - Note: at the time of adding, the file is JPEG data carrying a `.png` extension. Most renderers handle this without issue; a future tidy-up could rename it to `.jpg` or re-export as a real PNG.

## Publication figures

The figures referenced from the publication source are in place as SVG files. They are JPEG images embedded inside SVG containers (from the source publication pipeline), which is why the file extension is `.svg` but the content is raster.

- `Image_2.svg` — section 4.3, first illustrative market relationships diagram
- `Image_3.svg` — section 4.3, second illustrative market relationships diagram
- `Image_4.svg` — section 12.9, flow-down of responsibilities to a relying party

Alt text for these figures is carried on the Markdown image references in the relevant section files themselves. Longer-form text descriptions could be added as supporting material in a future accessibility pass.

## Reserved filenames for future banner images

The following filenames are reserved as empty placeholder files so that if additional top-level banner illustrations are added later, references in the repository can be wired up without any filename churn. They are not currently referenced from any Markdown file.

- `uk-certifid-colour-background.png`
- `versioned-documents-overview.png`
- `standards-and-interoperability.png`
- `uk-certifid-mark.png`

Filenames must not be changed, renamed, lowercased or hyphenated. If any of these are no longer wanted, the corresponding placeholder file can be deleted.

## Back

- [Repository home](../README.md)
