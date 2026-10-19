Legal

# Terms of use

Please read these terms carefully before using bStats. By accessing or using any part of
the Service, you agree to be bound by these terms of use.

**Last updated:** 2025/12/04

## 1. Introduction

**bStats** ("bStats," "we," "us," or "our") is an open-source analytics
service that plugin/mod developers integrate into their software to gather technical
usage data. These terms of use (the "**Terms**") govern your access to
and use of:

- The bStats website (**bStats.org**) and any related subdomains (the
  "**Site**").
- The bStats code, including the Metrics class embedded in plugins (the "**bStats Code**" or "**Metrics Class**").
- Any other services, dashboards, or tools provided by bStats (collectively, the "**Service**").

By accessing or using any part of the Service, you agree to be bound by these Terms.
If you do not agree, you must discontinue use of the Service immediately.

## 2. Definitions

- **Developer**: A person or entity that includes the Metrics Class
  in a plugin/mod.
- **Server Operator**: A person or entity operating a game server
  (e.g., a Minecraft or Hytale server) running a plugin that includes the Metrics Class.
- **User**: Any individual or entity that accesses the Site or
  Service, including Developers, Server Operators, and visitors.
- **Custom Charts**: Developer-defined charts or fields submitted to
  the Service.

## 3. Scope and eligibility

### Who is covered

- **Plugin developers**
- **Server operators**
- **Website visitors**

### Age restrictions

The Service is not intended for use by anyone under the age of 13. If you are
located in a jurisdiction with a higher digital age of consent (generally 13-16 in
the EEA/UK), you must meet that age. If you are under the applicable age, you may
use the Service only under the supervision of a parent or legal guardian who agrees
to be bound by these Terms on your behalf. We do not knowingly collect personal
information from children under 13. If we learn that we have collected personal
information from a child under 13, we will delete it. Any account creation must be
performed only by individuals who meet the applicable age threshold. Please see our [privacy policy](./privacy-policy) for more information or to learn how to contact us regarding children's data.

## 4. Open-source licensing and ownership

**Open-source code:** The bStats Code is provided under the *MIT License*. Your rights to the bStats Code are governed by that license,
which is separate from these Terms.

**Plugins:** Developers retain all rights to their plugin/mod code. Nothing
in these Terms transfers ownership of any plugin intellectual property to bStats.

## 5. Metrics Class integrity (use of the Service)

While the open-source license for the bStats Code may permit modifications, your
access to and use of the *Service* (i.e., bStats' hosted collectors, dashboards, and related
infrastructure) is expressly conditioned on leaving the **Metrics Class** unmodified, *except* for package-name relocation. The only permitted change
is to relocate the package name (either by manually editing the `package` declaration or by using relocation/shading that performs *package relocation only*).

- **All other modifications are prohibited.** You must not alter source
  or bytecode, rename classes, methods, or fields, change logic or data collected,
  inject additional endpoints, wrap or intercept calls, or otherwise modify the Metrics
  Class. You must exclude the Metrics Class from obfuscation, shrinking, minification,
  instrumentation, or any transformation beyond package relocation.
- **Opt-out integrity.** You must not remove, disable, hide, or interfere
  with the bStats opt-out or any related configuration checks.
- **Forks sending data to non-bStats servers.** If you modify the
  Metrics Class (or bStats Code) to post data to any server other than bStats'
  official collectors, you may *not* use the Service. In that case you must:
  (i) remove all bStats branding, names, and identifiers from code, user interfaces,
  and documentation; and (ii) not use, ship, read, or modify any bStats configuration
  file(s) or directories (e.g., any “bStats” config), and ensure the modified code
  does not contact bStats infrastructure.
- **Use the public APIs instead of modifying the Metrics Class.** If you
  need additional telemetry (e.g., Custom Charts), implement it via your plugin/mod
  using the documented bStats APIs without altering the Metrics Class itself.
- **Enforcement.** We may block, throttle, or otherwise restrict clients
  that violate this section and may remove or disable related dashboards or datasets.
- **License clarification.** This section governs access to the
  Service and does not limit your rights under the applicable open-source license
  when using the code *without* connecting to the Service.

## 6. Prohibited data (including Custom Charts)

Do not configure or use bStats to collect, submit, or transmit data that is personal
or sensitive, including but not limited to:

- IP addresses (full or truncated), device or hardware identifiers, MAC addresses,
  advertising IDs;
- Player usernames, player UUIDs/IDs (including hashed or salted), emails, account
  IDs from any platform;
- Chat logs, command history, free-text fields likely to contain personal data;
- Geolocation (including GPS coordinates), precise location, or addresses;
- Server IP addresses/domains or other sensitive server-specific information;
- Secrets, API tokens, private keys, passwords, or authentication material.

bStats reserves the right to investigate and remove any plugins or Developers who
misuse the Service by collecting prohibited data, and to delete offending datasets.

## 7. Data roles and Developer obligations

1. **Roles.** bStats provides telemetry infrastructure and dashboards
   and designs the Service to avoid processing personal data. For service and
   security data that bStats collects directly (e.g., server logs, abuse signals),
   bStats acts as an independent controller. bStats is *not* a processor for
   Developer-submitted telemetry. No controller-processor relationship is created by
   your use of the Service, and bStats will not enter into a Data Processing Agreement
   (DPA). If you require a processor or a DPA, you must not use the Service.
2. **Obligations.** For any data you send, you represent that you have
   a lawful basis to collect and transmit such data and that required notices have been
   provided.
3. **No personal data.** You will not submit personal data or data reasonably
   linkable to an individual. If you accidentally submit such data, you must notify
   us promptly and remove the submission.

## 8. User responsibilities

- **Compliance with laws:** You will use the Service only in compliance
  with all applicable laws and regulations.
- **Accurate information:** If you create an account, you must provide
  accurate information and safeguard your credentials.
- **No abuse of Service:** You will not access non-public areas, interfere
  with infrastructure, reverse engineer, or circumvent security features.

## 9. Privacy policy

Your use of the Service is also governed by our [privacy policy](./privacy-policy), which
explains how we collect, use, and protect data. In the event of a conflict between
these Terms and our privacy policy regarding data handling, the privacy policy
prevails.

## 10. Service changes and availability

bStats is open-source and maintained by volunteers and contributors. We may modify,
suspend, or discontinue the Site or any feature of the Service at any time without
liability. We do not guarantee that the Service or code will be free from defects or
available without interruption.

## 11. Security and vulnerability disclosure

We implement reasonable technical and organizational measures appropriate to the
nature of the Service. Do not perform testing that could disrupt the Service. Report
vulnerabilities privately and allow a reasonable remediation period before public
disclosure.

## 12. API, rate limits, and anti-scraping

We may publish or change API endpoints, quotas, and rate limits at any time. You may
not scrape, bulk export, or rehost dashboards or datasets without prior written
consent. Caching for personal or project use is allowed within published limits and
must respect robots directives and caching headers.

## 13. Intellectual property; complaints; trademarks

- **Content ownership:** The Site and Service may display plugin names,
  versions, and aggregated metrics. Third-party names and marks remain the property
  of their respective owners.
- **Notice and takedown:** If you believe content on the Service infringes
  your rights, send us a notice with: (i) identification of the work; (ii) the infringing
  material/URL; (iii) your contact details; and (iv) a statement under penalty of perjury
  that you are authorized to act. We may remove or disable access and notify the submitter.
- **Trademarks:** "bStats" and related logos are our trademarks. You may
  not use them without prior written permission, except for nominative fair use.

## 14. Disclaimers of warranties

- **"As-Is" and "As Available":** The Service and all associated software
  (including bStats Code) are provided on an "as-is" and "as available" basis.
- **No warranty:** To the fullest extent permitted by law, we disclaim
  all warranties and conditions, whether express, implied, statutory, or otherwise,
  including implied warranties of merchantability, fitness for a particular purpose,
  and non-infringement.
- **Open-source nature:** We do not guarantee that the Service or code
  will be free from defects or available without interruption.

## 15. Limitation of liability

- **Exclusion of damages:** To the fullest extent permitted by law, bStats
  shall not be liable for any indirect, incidental, consequential, special, or exemplary
  damages, loss of data, loss of profits, or costs of procurement of substitute goods
  or services arising out of or related to your use of (or inability to use) the Service.
- **Aggregate liability cap:** In no event shall bStats' total liability
  to you for all claims arising out of or relating to these Terms exceed the amount
  you paid (if any) for using the Service in the preceding twelve (12) months (or EUR
  €0.00 if you have not paid any fees).
- **Exception:** Some jurisdictions do not allow the limitation or exclusion
  of liability for certain damages; in such cases, the liability will be limited to
  the greatest extent permitted by law. Nothing in these Terms limits or excludes liability
  of bStats (a) for intent or gross negligence; (b) for injury to life, body or health;
  (c) under the German Product Liability Act; or (d) where we have assumed a guarantee
  or fraudulently concealed a defect. In the event of simple negligence, we are liable
  only for breach of such contractual duties the fulfillment of which is essential
  for the proper performance of the contract and on the observance of which you regularly
  rely (wesentliche Vertragspflichten); in such cases our liability is limited to the
  foreseeable damage typical for the contract. Otherwise, liability is excluded to
  the extent permitted by law.

## 16. Indemnification

You will defend, indemnify, and hold harmless bStats and its contributors from and
against all claims, liabilities, damages, losses, and expenses (including reasonable
legal fees) arising out of or related to: (a) your use of the Service; (b) your
breach of these Terms; or (c) any data you submit to the Service.

## 17. Third-party services

The Service may rely on or link to third-party services (e.g., Discord, GitHub,
hosting/CDN providers). Your use of those services is subject to their terms, and we
are not responsible for them.

## 18. Public stats and content license

You acknowledge that plugin names, versions, and aggregated usage metrics may be
publicly displayed on the Site. To the extent necessary for that display, you grant
bStats a worldwide, non-exclusive, royalty-free license to host, display, and
reproduce such content in connection with the Service.

## 19. Export control and sanctions

You represent that you are not located in, resident of, or organized under the laws
of a country or territory subject to comprehensive sanctions and that you are not a
denied or restricted party. You will not use the Service for prohibited end uses
under applicable export laws.

## 20. Termination

- **By you:** You may stop using the Service at any time. If you have
  an account, you may delete it.
- **By us:** We may suspend or terminate your access to the Service or
  specific functionality if we reasonably believe you have violated these Terms or
  engaged in fraudulent or illegal conduct.
- **Effect:** Upon termination, your right to access or use the Service
  ceases immediately. Clauses that by their nature survive termination (e.g., disclaimers,
  limitation of liability, indemnification) remain in effect.

## 21. Governing law and jurisdiction

These Terms are governed by and construed in accordance with the laws of the Federal
Republic of Germany, without regard to conflict-of-law principles. You agree that
any dispute arising out of or relating to these Terms shall be submitted to the
exclusive jurisdiction of the competent courts located in Germany, unless otherwise
required by a mandatory law of your jurisdiction.

## 22. Changes to these Terms

We may update or modify these Terms from time to time. The "Last updated" date
indicates when changes were made. Your continued use of the Service following any
changes signifies your acceptance of the revised Terms. If you do not agree to the
changes, you should discontinue use before the effective date.

## 23. Force majeure

We are not liable for delays or failures due to events beyond our reasonable
control, including outages, DDoS attacks, acts of government, war, labor disputes,
or natural disasters.

## 24. Assignment

You may not assign or transfer these Terms without our prior written consent. We may
assign or transfer these Terms in connection with a merger, acquisition, or transfer
of assets.

## 25. Entire agreement; severability; interpretation

- **Entire agreement:** These Terms, together with our privacy policy
  and any applicable open-source license terms, constitute the entire agreement between
  you and bStats regarding the Service.
- **Severability:** If any provision of these Terms is held invalid or
  unenforceable, that provision will be enforced to the maximum extent permissible,
  and the remaining provisions will remain in full force and effect.
- **No waiver:** Failure to enforce a provision is not a waiver of the
  right to do so later.
- **Headings; translations:** Headings are for convenience only. If these
  Terms are translated, the English version controls (unless a mandatory law requires
  otherwise).

## 26. Support and contact

- **Support and issue tracking:** For help or bug reports, reach out
  via our [Discord channel](https://discord.gg/qTXtXuf) or open an issue in our [GitHub repository](https://github.com/Bastian/bStats).
- **Legal inquiries / DPA requests:** Please refer to the contact information provided in the bStats [privacy policy](./privacy-policy).

Thank you for using bStats! If you have any questions about these Terms or the
privacy policy, please contact us using the channels above.
