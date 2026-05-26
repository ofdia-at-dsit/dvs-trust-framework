> [!CAUTION]
> This repository is a workspace copy for navigation, drafting, version control and collaboration. It is not the official statement of government policy and must not be relied on as such. For the official published policy, see the [UK digital verification services trust framework 1.0 on GOV.UK](https://www.gov.uk/government/publications/uk-digital-verification-services-trust-framework-1-0/uk-digital-verification-services-trust-framework-1-0-pre-release).

<a id="section-7"></a>

## 7. Rules for holder service providers

7.a. Holder service providers must follow these rules and those in [Part 3](../part-3/README.md#part-3).

<a id="section-7_1"></a>

### 7.1. Holding identities and attributes

7.1.a. Your service must store information securely and ensure it is not illegitimately accessed or changed. You must prevent any unauthorised persons from accessing a user’s holder service account by following the [guidance on how to use authenticators to protect an online service](https://www.gov.uk/government/publications/how-to-use-authenticators-to-protect-an-online-service-1-0). This is also known as Good Practice Guide (GPG) 44.

<a id="example-2"></a>

>
> ##### Illustrative example 2
>
> George is travelling on holiday abroad with her three-year-old child. She holds both of their digital boarding passes, issued by the airline, as attributes in her preferred digital wallet app.
>
> The wallet has been certified as a holder service and is protected by an appropriate form of biometric authentication.
>
> Airline staff request their boarding passes at the gate. George has to scan her face on her device before it will allow her to present the boarding pass. This ensures that only George can access the information stored in her holder service. George’s child would not be able to access their boarding pass without her.
>

7.1.b. You must be able to provide [GPG 44](https://www.gov.uk/government/publications/how-to-use-authenticators-to-protect-an-online-service-1-0) the levels of protection your service achieved in a specific transaction to relying parties and other services you work with. You could additionally provide which specific authenticators were used and what quality level was achieved. For example, metadata you share could specify that medium-quality passkey was used by a user to authenticate into your service.

7.1.c. Your service must also be able to provide the following information to relying parties and other services you work with:

- whether an identity or attribute you hold comes from a registered service;

- whether an identity you hold meets specific [GPG 45](https://www.gov.uk/government/publications/how-to-check-someones-identity-1-0) level(s) of confidence and identity profile(s), if this information is available to you;

- whether an attribute you hold has been reliably linked to a person. This is called binding. If you bind the attribute, you must follow the rules on binding in the [attributes guidance](https://www.gov.uk/government/publications/how-to-create-bind-and-share-attributes-1-0) to do so; and

- whether the person presenting an identity or attribute is the person to whom it was originally issued. If they are not, then you could check if the user has the necessary authority to act on someone else’s behalf in line with [section 12.2.](../part-3/12-service-requirements.md#section-12_2) on delegated authority.

<a id="example-3"></a>

>
> ##### Illustrative example 3
>
> Gabrielle is trying to prove she is a registered university student to access a student-only discount at a bookstore. She stores a digital identity in a holder service app. The identity includes attributes derived from authoritative university data by a registered attribute service and the app is protected by an appropriate form of biometric authentication.
>
> Bookstore staff request to see Gabrielle’s proof of student status. Gabrielle has to scan her face in the app before it will allow her to present her student status. This confirms it is Gabrielle trying to present her own information. Gabrielle’s friend would not be able to access her information.
>
> Gabrielle then holds her phone to a scanner presented by the bookstore staff. Metadata exchanged in the scan confirms that the attribute came from a registered service, that it was issued to Gabrielle and that she is the one presenting it here and now. The bookstore can be sure Gabrielle is a current student and eligible for the discount.
>

7.1.d. You must also make clear to relying parties and other services you work with whether an identity or attribute you hold has expired and/or been lost, stolen or revoked, if this information is available to you. For instance, you could check the status of an attribute or credential with an authoritative source before it is presented.

<a id="section-7_2"></a>

### 7.2. Reusing a verified digital identity or attribute in a holder service

7.2.a. If you are an identity or attribute service provider and want to allow a user to repeatedly assert information about themself that you have verified, you must store the digital identity and/or attributes in a holder service. Your service must follow the rules in [section 10.3.](../part-3/10-inclusivity-accessibility-and-service-design.md#section-10_3) on confirming a user’s understanding before you use their data to do this.

7.2.b. You must be able to show the user what level(s) of confidence and identity profile(s) their identity meets according to [GPG 45](https://www.gov.uk/government/publications/how-to-check-someones-identity-1-0), in an easily accessible way, if that information is available to you.

<a id="example-4"></a>

>
> ##### Illustrative example 4
>
> Hayley has already had her identity checked to a medium level of confidence with a high street bank to sign up to their online banking app.
>
> Following the trust framework, the bank used the details provided by Hayley during the sign-up process to create a verified digital identity. Hayley can store this identity in the bank’s holder service, and the bank makes it easy for Hayley to check which level of confidence under [GPG 45](https://www.gov.uk/government/publications/how-to-check-someones-identity-1-0) her identity reaches.
>
> Hayley can then use this service in the future to prove her identity and share attributes without doing an identity check from scratch.
>

<a id="example-5"></a>

>
> ##### Illustrative example 5
>
> In the future, Patrick may be able to store a Qualified Certificate (QC) in a holder service. A qualified trust service provider (QTSP) will have bound his verified identity to this QC. Patrick could then present this QC from his holder service, allowing a relying party to validate his e-Signature.
>

<a id="section-7_3"></a>

### 7.3. Managing a user’s holder service account

7.3.a. You must have processes to revoke, suspend, close, recover and make changes to a user’s holder service account. This includes supporting the appropriate identity and/or attribute services, which could be another service you provide, to make legitimate changes to information held in a user’s holder service account. For example, if a digital credential is altered or revoked by its issuer, you must be able to reflect these changes in the user’s holder service account.

7.3.b. You must close a holder service account if:

- the user wants to close it;

- you have evidence it was created fraudulently, including using a synthetic identity; or

- you become aware of the user’s death, although you may leave the user’s account open for a limited time if needed to manage requests related to their account, for example to manage settling estates.

7.3.c. You must have processes in place to take action against a user who does not follow the terms of use they agreed to. These must include a process for closing their holder service account and preventing access to your service if the issue cannot be resolved.

7.3.d. If an identity in a user’s holder service account has been inactive for 14 months, the user’s identity must be checked again following [GPG 45](https://www.gov.uk/government/publications/how-to-check-someones-identity-1-0) before the inactive identity can be used or shared again. This check must meet either the same level of confidence originally met or a higher level of confidence than the one originally met.

<a id="section-7_3_1"></a>

#### 7.3.1. Notifying a user of changes to their holder service account

7.3.1.a. You must have a process in place to notify the user of any changes to their holder service account as well as any identities and attributes held within it. This includes any legitimate changes made by the identity or attribute service that issued it. You must also have a process in place to notify the user if you have received a request to close their holder service account. Your notification processes must notify the user of requested changes to their account using more than one channel, and must not undermine any of the rules on risk management ([section 11.7](../part-3/11-operational-requirements.md#section-11_7)), fraud management ([section 12.4.](../part-3/12-service-requirements.md#section-12_4)) and responding to incidents ([section 11.5.](../part-3/11-operational-requirements.md#section-11_5)).

<a id="example-6"></a>

>
> ##### Illustrative example 6
>
> Company A, which provides a holder service, maintains a list of email addresses and phone numbers for users of its holder service. As a result, when changes are made to a user’s holder service account, Company A uses email and text message to notify the user, as well as on-device push alerts.
>
> Company B, which also provides a holder service, has designed the service so it is impossible to link any data it holds about users with any specific user’s account. As a result, when changes are made to a user’s holder service account, Company B alerts the user with in-app pop-ups and on-device push notifications.
>

7.3.1.b. You must provide users with means to respond to these notifications, for instance by querying the change or closure.

7.3.1.c. If a user wants to change the contact details associated with their holder service account, you must authenticate the user before allowing them to make these changes.

---

**Repository navigation**

[← Previous: 6. Rules for attribute service providers](06-rules-for-attribute-service-providers.md) · [Part README](README.md) · [Trust Framework 1.0](../README.md) · [Repository home](../../README.md) · [Next: 8. Rules for orchestration service providers →](08-rules-for-orchestration-service-providers.md)
