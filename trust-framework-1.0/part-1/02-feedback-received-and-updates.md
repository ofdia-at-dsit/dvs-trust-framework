> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published policy, see the [UK digital verification services trust framework 1.0 on GOV.UK](https://www.gov.uk/government/publications/uk-digital-verification-services-trust-framework-1-0/uk-digital-verification-services-trust-framework-1-0-pre-release).

<a id="section-2"></a>

## 2. Feedback received and updates

2.a. The trust framework is being developed iteratively. This allows for testing to ensure that its rules are appropriate, proportionate and deliver on the government’s [digital identity principles](https://www.gov.uk/government/consultations/digital-identity/outcome/digital-identity-call-for-evidence-response#:~:text=5.2%20A%20Principles%2Dbased%20approach). Iteration also helps ensure alignment with international best practice, as new standards are issued and the digital identity market matures.

2.b. In line with [section 31 of the Act](https://www.legislation.gov.uk/ukpga/2025/18/section/31), the [Information Commissioner’s Office](https://ico.org.uk/) (ICO) and other appropriate stakeholders across industry, civil society, and the public sector have been consulted on the content of the trust framework through written surveys and working groups. The trust framework will continue to be updated as changes are needed, and the market develops.

<a id="section-2_1"></a>

### 2.1. Changes made for the 1.0 publication

2.1.a The previous, [gamma (0.4) publication of the trust framework](https://www.gov.uk/government/publications/uk-digital-identity-and-attributes-trust-framework-04) was designed to significantly uplift the minimum standards services adhere to. This publication (1.0) of the trust framework is intended to iteratively build upon that high baseline. As such, the majority of the changes in this version of the trust framework are in the [supporting documents](https://www.gov.uk/government/collections/uk-digital-identity-and-attributes-trust-framework-supporting-documents) that underpin the trust framework.

2.1.b. This rest of this section sets out key changes to this document and its supporting documents in this publication.

<a id="section-2_1_1"></a>

#### 2.1.1. The UK CertifID trust mark 

2.1.1.a. Providers certified against this publication, and listed as such on the [register of digital identity and attribute services](https://www.digital-identity-services-register.service.gov.uk/register) will, for the first time, be able to use the new UK CertifID trust mark (the ‘trust mark’). Wherever people or businesses see the trust mark displayed, they can be confident that the product or service can be trusted to be secure, meeting the rules set out in the trust framework and subject to oversight by OfDIA.  

2.1.1.b. The Act enables the Secretary of State to issue the licence to use the trust mark to registered services. Issuance is undertaken by OfDIA on the Secretary of State’s behalf. [Section 14](../part-3/14-the-uk-certifid-trust-mark.md#section-14) sets out the new rules governing when and how the trust mark can be used. 

<a id="section-2_1_2"></a>

#### 2.1.2 Alignment with the Data (Use and Access) Act 2025

2.1.2.a. As set out in [section 0](../00-version-and-certification-validity-notes.md#section-0), as this is the first revised statutory trust framework publication under the Act, we have aligned its title with the [term it is given in the Act: ‘DVS trust framework’](https://www.legislation.gov.uk/ukpga/2025/18/part/2/crossheading/dvs-trust-framework-and-supplementary-codes). All previous publications of the trust framework were titled the ‘UK digital identity and attributes trust framework’. 

2.1.2.b. To align the trust framework with the [scope it is given in the Act](https://www.legislation.gov.uk/ukpga/2025/18/section/27), we have also focused the trust framework’s rules on the identities and attributes of natural persons, i.e. individuals, rather than companies or organisations. 

<a id="section-2_1_3"></a>

#### 2.1.3. Holder service providers 

2.1.3.a. During policy testing, we heard that additional rules were needed to better support relying parties and other services to accept digital identities and attributes stored in [holder services](../part-2/07-rules-for-holder-service-providers.md#section-7). 

2.1.3.b. To achieve this, we have added new rules for holder service providers to help relying parties understand and integrate with their services by requiring that they are able to share metadata about confidence in identities, authentication methods, identity and attribute provenance, and binding to the user. More details are available in [section 7](../part-2/07-rules-for-holder-service-providers.md#section-7) on holder service providers. 

2.1.3.c. To align with [the National Cyber Security Centre (NCSC)’s commitment to encourage the adoption of passkeys](https://www.ncsc.gov.uk/collection/ncsc-annual-review-2025/chapter-03-keeping-pace-with-evolving-technology/passkeys), we’ve made clear how syncable authenticators (of which passkeys are an example) can be used as part of [our authentication guidance](https://www.gov.uk/government/publications/how-to-use-authenticators-to-protect-an-online-service-1-0), which holder service providers are required to follow. 

<a id="section-2_1_4"></a>

#### 2.1.4. Orchestration service providers 

2.1.4.a. This publication introduces our first dedicated rules for orchestration service providers. There are now requirements in [section 8](../part-2/08-rules-for-orchestration-service-providers.md#section-8) requiring orchestration service providers to be able to confirm whether the services they orchestrate are on the DVS register. This reflects the growing significance of confirming DVS registration in the market. We provide the option for this be done with reference to a cache of the register, or to be done against the live register. This anticipates the introduction of programmatic capability for the register later this year, which will allow real-time checks of the register using an application programming interface (API).

2.1.4.b. The technical options for orchestrating identities and attributes otherwise remain broad and open to innovation. We expect the role of orchestration services to become more important over the coming years, and we will continue to monitor the market and to determine whether some orchestration service providers would be better served by new rules, new sub-roles, or a new role entirely in a future publication of the trust framework.

<a id="section-2_1_5"></a>

#### 2.1.5. Vouching and digital evidence

2.1.5.a. We have amended the supporting documents to provide a clearer role for secure vouching in identity checking at lower levels of confidence. The [vouching guidance](https://www.gov.uk/government/publications/how-to-create-a-vouch-as-evidence-of-someones-identity-1-0) has been rewritten to provide a clearer way for a vouch to be scored as evidence as part of an identity checking process. The rewritten vouching guidance retains some requirements from previous versions, for example the requirement for the person vouching to be in a listed position of authority. It sets a number of new requirements, for example to specify which scores a vouch can be given in accordance with the identity checking guidance.

2.1.5.b. The [identity checking guidance](https://www.gov.uk/government/publications/how-to-check-someones-identity-1-0) has also been clarified to make clearer how digital evidence can be scored for validity. While the substance of the rules has not been changed, which rules apply to digital evidence, which apply to physical evidence, and which apply to both has been made clearer.

<a id="section-2_1_6"></a>

#### 2.1.6. The data schema 

2.1.6.a. The 1.0 publication is accompanied by [an updated data schema](https://www.gov.uk/government/publications/uk-digital-verification-services-trust-framework-data-schema-1-0). The schema is newly reformatted to improve usability, with a revised and modernised data model, data dictionary and data taxonomy. We've aligned, where appropriate, with major data sharing and presentation standards to make the schema a more practical resource for industry adoption and expanded its scope to cover priority areas and data points from across government and industry. 

2.1.6.b. As in previous publications, use of the data schema remains optional for certified services. 

<a id="section-2_1_7"></a>

#### 2.1.7. Interaction between services and roles 

2.1.7.a. The [gamma (0.4) publication](https://www.gov.uk/government/publications/uk-digital-identity-and-attributes-trust-framework-04) introduced [the component service provider role](../part-2/09-rules-for-component-service-providers.md#section-9) to enable providers who specialise in particular parts of the identity, attribute and authentication process to certify the parts that they provide, so they can more easily integrate into other certified services. 

2.1.7.b. This has highlighted the reliance that certified services can have on the certification of those in their supply chain. To mitigate the risks of this reliance, we've set new requirements in [section 11.7](../part-3/11-operational-requirements.md#section-11_7) for all providers to use their risk management framework to capture the risk of services they rely on losing their certification, and the risk to others if they lose their certification. 

2.1.7.c. Knowing which roles a DVS is certified against helps those who want to use that DVS to understand if it meets their needs. In order to give clarity on the service offerings of DVS providers to those they work with, we have added new rules in [sections 4.1.c. and 4.1.d.](04-how-organisations-participate-in-the-trust-framework.md#section-4_1) which mean that a service certifying as [an orchestration service](../part-2/08-rules-for-orchestration-service-providers.md#section-8) or as a [component service](../part-2/09-rules-for-component-service-providers.md#section-9) cannot have a concurrent certification under any other role.

2.1.7.d. If you provide a component service or orchestration service alongside other roles, you will need to have the component service and/or orchestration service certified separately. This will help those you work with understand what has been certified when they work with you. The [identity service provider](../part-2/05-rules-for-identity-service-providers.md#section-5), [attribute service provider](../part-2/06-rules-for-attribute-service-providers.md#section-6) and [holder service provider](../part-2/07-rules-for-holder-service-providers.md#section-7) roles remain certifiable alongside one another and in any combination.

<a id="section-2_1_8"></a>

#### 2.1.8. Navigability of supporting documents

2.1.8.a. The [supporting documents](https://www.gov.uk/government/collections/uk-digital-identity-and-attributes-trust-framework-supporting-documents) for the trust framework have now all been given a version number so that the trust framework can specify which version services must follow as part of their certification against this trust framework publication and future publications.

2.1.8.b. Every paragraph is now numbered across the supporting documents to make them as navigable as this document and enable cross-referencing between documents.

2.1.8.c. The [guidance on attributes](https://www.gov.uk/government/publications/how-to-create-bind-and-share-attributes-1-0), which was previously spread across three supporting documents, has been consolidated into one, and the [identity checking guidance](https://www.gov.uk/government/publications/how-to-check-someones-identity-1-0) has been restructured so some technical elements which were spread out across sections and across different webpages are all contained in annexes to the main publication. The [guidance on delegated authority](https://www.gov.uk/government/publications/how-to-check-whether-someone-has-delegated-authority-1-0) has also been revised to better link to the guidance on identity checking.

<a id="section-2_1_9"></a>

#### 2.1.9. Inclusion, accessibility and service design 

2.1.9.a. Rules in [section 10](../part-3/10-inclusivity-accessibility-and-service-design.md#section-10) on inclusion and accessibility that, previously, only identity service providers, attributes service providers and holder service providers were required to follow, are now mandatory for all provider types. This means that providers of all types will now be required to submit an inclusion monitoring report and demonstrate that they follow accessible design standards in their service.

2.1.9.b. Rules on confirming user understanding, previously set out alongside privacy rules, are now set out in [section 10](../part-3/10-inclusivity-accessibility-and-service-design.md#section-10_2) alongside the inclusion and accessibility rules. This emphasises that these rules are intended to inform service design, rather than simply as a part of a service’s compliance with the requirements of data protection legislation. 

<a id="section-2_1_10"></a>

#### 2.1.10. Security and fraud 

2.1.10.a The trust framework reflects that DVS providers have a role not only in preventing identity fraud, but also in supporting users who fall victim to it. Now that [Action Fraud has been replaced by Report Fraud](https://www.gov.uk/government/news/report-fraud-new-service-from-city-of-london-police), we have incorporated requirements previously set out in Action Fraud guidance directly into the main body of the trust framework in [section 12.5.5](../part-3/12-service-requirements.md#section-12_5_5), tailoring and extending them. We will review whether there are new Report Fraud materials we can point to in future publications. 

<a id="section-2_1_11"></a>

#### 2.1.11. Prohibited data processing 

2.1.11.a. We have extended the rules in [section 12.7.3](../part-3/12-service-requirements.md#section-12_7_3) which prohibit the processing of identity and attribute data for certain purposes. These rules now apply to metadata about this data, not just the identity and attribute data itself. This metadata can reveal things about a person much like identity or attribute data itself can. 

---

**Repository navigation**

[← Previous: 1. Introduction](01-introduction.md) · [Part README](README.md) · [Trust Framework 1.0](../README.md) · [Repository home](../../README.md) · [Next: 3. Terms and definitions →](03-terms-and-definitions.md)
