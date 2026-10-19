Legal

# Privacy policy

bStats collects only the information we need to provide useful metrics. Below you'll
find details for both the plugin-side telemetry and the website account system.

**Last updated:** 2025/12/04

## bStats plugin privacy policy

If you are a server owner installing a plugin that uses bStats or a casual site
visitor, this policy explains what data is collected, why, and how long it is
retained. If you are a plugin developer registering an account on the bStats.org
website, please refer to the **bStats website privacy policy** below.

### 1. Who we are (data controller)

**bStats** ("we," "us," or "our") refers to the open-source service that
plugin developers embed into their game server plugins/mods for analytics. The data controller
is:

<blockquote><p class="no-copy"><strong><span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">і​tѕ​а​Β</span><span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">​рр​О​ ​nа</span><span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">nn​аm​​rе​</span></strong><br/> <span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">lе​g​еі​​р​S</span><span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">​а​rtѕ​</span><span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">6​ ​еß​</span><br/> <span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">​67​0​9</span><span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">​üF​ 2​</span><span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">һ​tr</span>, <span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">​у​nа​m​rе​G​</span><br/> Email: <strong class="no-copy"><span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">а​t​n​ос</span><span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">​t​а​] ​t​с</span><span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">ѕb ​[</span><span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">ѕ​​t​аt</span><span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">​[t​​о​d​]</span><span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">g​r​​о​</span></strong></p></blockquote>

### 2. Scope: What this policy covers

- **bStats plugin embedding**: This policy covers data collected when
  plugins that include the bStats script are run on a server.
- **Server owners**: Typically, you (as the server owner) do not
  provide any personal data to bStats; only technical data about the server
  environment is transmitted.
- **Custom metrics**: Developers can add custom charts or metrics
  beyond bStats' default collection. We prohibit collecting personal information.
  We remove or ban offending plugins/authors if we discover misuse.

### 3. Data we collect and why

1. **Technical server data**

   - **Examples**: Operating System (OS), Java version, CPU
     architecture, server version (e.g., Minecraft or Hytale version), plugin/mod
     version, and a pseudonymous server identifier for deduplication and
     anti-abuse.
   - **Purpose / legal basis**: Provide analytics to plugin
     developers and operate, protect, and improve the Service. For this
     processing, **bStats acts as an independent controller** relying on *legitimate interests* under the GDPR/UK GDPR. Developers
     remain separate controllers and must ensure they do not send personal data
     to bStats.
2. **IP address (short-term storage)**

   - bStats receives an IP address with each data transmission for
     rate-limiting and abuse prevention.
   - **Retention (our systems)**: IP addresses are stored for up
     to **60 minutes** solely to track request volume, then discarded.
     They are never linked to accounts or personal profiles.
   - **Legal basis**: Our legitimate interest in ensuring stable
     service, preventing spam/abuse, and securing our infrastructure.
3. **Prohibited personal data in custom metrics**

   - Developers must not send personal data (names, emails, IPs, device
     identifiers, or any data that can directly identify a natural person)
     via custom metrics. We remove or ban any misuse.

### 4. Legal bases for processing (GDPR/UK GDPR)

- **Legitimate interests**: Processing IP addresses briefly and using
  pseudonymous server identifiers to prevent abuse and measure plugin usage for
  service integrity and security.
- **Right to object**: Where we rely on legitimate interests, you may
  object at any time. Practically, server owners can disable telemetry (see
  Section 5).

### 5. How to opt out

- **Configuration file**: Each plugin that includes bStats typically
  generates a global config file. You can disable bStats here, preventing any
  further data transmission from any plugin.

### 6. Data retention

- **Server metrics**: Aggregated, de-identified metrics
  (non-personal) may remain in our databases indefinitely to track historical
  trends.
- **IP addresses (our systems)**: Stored only up to **60 minutes** in a rate-limiting mechanism, then automatically erased.
- **Provider security logs**: Our CDN/WAF and hosting providers may
  retain limited security logs for short periods consistent with their policies
  and our configurations. We configure the shortest practical retention and do not
  use provider security logs to profile users.
- **Backups**: If backups are kept, IP addresses are typically not
  stored long-term. Any short-term logs are overwritten periodically.

### 7. Security measures

- **Secure transmission**: Data is sent over secure channels
  (HTTPS/SSL).
- **Access controls**: Only authorized personnel (e.g., site
  maintainers) can access raw logs.
- **Infrastructure safeguards**: We employ measures such as
  firewalling, intrusion detection, and regular security reviews where feasible.

### 8. Third-party services, subprocessors, and international transfers

- **Hosting**: Our infrastructure is hosted by [GameHosting.it](https://www.gamehosting.it/), which processes data
  on our behalf.
- **Cloudflare**: Traffic is routed through Cloudflare's network for
  performance and security. Cloudflare may temporarily process IP addresses and
  related connection data and set strictly necessary cookies.
- **International transfers**: Where data is transferred outside your
  jurisdiction (e.g., EU/EEA/UK to other countries), we rely on an appropriate
  mechanism: adequacy decisions (including recognized frameworks), the EU 2021
  Standard Contractual Clauses (and UK Addendum/IDTA, as applicable), and routine
  transfer risk assessments. We apply encryption in transit, strict access
  controls, and data minimization.

### 9. Your rights (GDPR and similar laws)

Depending on your local laws (e.g., GDPR in the EU/UK), you may have rights over
personal data that we hold or process.:

- **Access**: Confirm whether we process your personal data.
- **Erasure/rectification**: Given the 60-minute retention window,
  data will likely already be purged, but you can still contact us.
- **Objection**: Object to processing based on legitimate interests;
  we will honor objections unless we have compelling grounds.
- **Complaint**: Lodge a complaint with your local supervisory
  authority.

We respond to GDPR/UK GDPR requests within one month (extendable where permitted).

### 10. Children's privacy

bStats does not knowingly collect personal data from children under the age of 13
(or 16 in certain jurisdictions). The service is generally aimed at adult server
owners and plugin developers. If you believe a minor's data was submitted, please
contact us at **а​t​n​ос​t​а​] ​t​сѕb ​[ѕ​​t​аt​[t​​о​d​]g​r​​о​**.

### 11. Prohibited personal data in custom metrics and enforcement

- If you suspect a plugin is using bStats to gather personal data, please contact
  us at **а​t​n​ос​t​а​] ​t​сѕb ​[ѕ​​t​аt​[t​​о​d​]g​r​​о​**. We will investigate and may remove or ban any misuse.

### 12. California privacy disclosures (CPRA/CCPA)

- **Categories collected**: Identifiers (IP address in transient
  security logs, Internet/technical information (server telemetry and connection
  metadata).
- **Purposes**: Security/anti-abuse, service provision, and plugin
  analytics.
- **Sensitive personal information**: Not sought or used.
- **Sale/sharing**: We do not sell or share personal information
  as defined by the CPRA and do not engage in cross-context behavioral advertising.
- **Rights**: Access, deletion, correction, and portability as
  applicable. We will verify your request (e.g., by account login or request
  metadata) and respond within 45 days (extendable as allowed).

### 13. Law enforcement and legal requests

We may preserve and disclose information if required by law or in good-faith belief
that such action is reasonably necessary to comply with legal obligations, respond
to lawful requests, or protect the rights, property, or safety of bStats, our users,
or the public.

### 14. Changes to this plugin privacy policy

We may modify this document from time to time to stay up to date with new legal
requirements or operational changes. We will post updated texts on our site with a
revised “Last updated” date and, where changes are material, provide reasonable
notice.

### 15. Contact information

If you have questions or concerns about how bStats processes server data, or if you
suspect misuse by a plugin developer, please email us: **а​t​n​ос​t​а​] ​t​сѕb ​[ѕ​​t​аt​[t​​о​d​]g​r​​о​**

**Last updated:** 2025/11/10

## bStats website privacy policy

### 1. Who we are (data controller)

This policy covers **bStats.org**, where plugin developers can register
an account to view or manage plugin analytics. The data controller is:

<blockquote><p class="no-copy"><strong><span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">і​tѕ​а​Β</span><span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">​рр​О​ ​nа</span><span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">nn​аm​​rе​</span></strong><br/> <span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">lе​g​еі​​р​S</span><span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">​а​rtѕ​</span><span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">6​ ​еß​</span><br/> <span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">​67​0​9</span><span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">​üF​ 2​</span><span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">һ​tr</span>, <span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">​у​nа​m​rе​G​</span><br/> Email: <strong class="no-copy"><span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">а​t​n​ос</span><span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">​t​а​] ​t​с</span><span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">ѕb ​[</span><span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">ѕ​​t​аt</span><span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">​[t​​оd]</span><span class="ltr-text" style="white-space:pre;direction:rtl;unicode-bidi:bidi-override;display:inline-block">g​r​​о​</span></strong></p></blockquote>

### 2. Scope: Website visitors and registered users

- **Public visitors**: Anyone can visit bStats.org and view plugin
  statistics without creating an account.
- **Registered users (plugin developers)**: You can create an account
  using a username and password and/or by linking an identity provider (e.g.,
  GitHub). **Providing an email address is optional**. If you choose
  to add an email, we will store it and its verification status to support account
  recovery and security.

### 3. Information collected

1. **Account registration & profile**

   - **Data**: Unique user ID; display name; optional username
     and display username; optional profile image; optional email address
     with verification status; account state (role, banned flag, ban
     reason/expiry); two-factor enabled status.
   - **Password security**: When you use a password, it is
     stored using an industry-standard password hashing algorithm with
     per-user salts. We never store plaintext passwords.
   - **Purpose/legal basis**: Contractual necessity to provide
     and secure your account; legitimate interests for platform security.
2. **Authentication sessions and audit**

   - **Data**: Session ID and token, creation/last activity
     timestamps, expiry time; **IP address** and **user agent** associated with the session.
   - **Cookies**: We set strictly necessary authentication
     cookies (e.g., a session token) to keep you logged in. If you opt to
     "remember" a 2FA device, we may set an additional strictly necessary
     cookie for that purpose.
   - **Purpose/legal basis**: Contractual necessity to maintain
     your session; legitimate interests in fraud prevention, abuse
     mitigation, troubleshooting, and account support.
3. **Linked accounts (OAuth/social sign-in)**

   - **Data**: Provider identifier and your account ID at that
     provider; tokens needed to sign you in (e.g., access/refresh/ID tokens
     and their expirations); authorized scopes.
   - **Use**: Solely to authenticate you and maintain the link
     you requested. We do not receive your password from those providers. You
     can unlink a provider at any time.
   - **Legal basis**: Contractual necessity and your
     request/consent to link a provider.
4. **Verification**

   - **Data**: One-time identifiers/tokens and their expiration
     for actions such as email verification, password reset, or passwordless
     sign-in.
   - **Use**: To complete the requested action; records are
     purged automatically when expired.
5. **Two-factor authentication (2FA)**

   - **Data**: 2FA secret and backup codes when you enable 2FA.
   - **Security**: Stored securely (hashed and/or encrypted) and
     used only to verify your login. You can disable 2FA or regenerate codes
     at any time.
   - **Legal basis**: Legitimate interests in account security
     and your request to enable 2FA.
6. **Cookies and related technologies**

   - **Session cookies**: Strictly necessary cookies keep you
     logged in and remember preferences. We do not use third-party
     marketing/behavioral tracking cookies.
   - **Security/edge cookies**: Our CDN/WAF may set necessary
     cookies for bot management and challenge passes.
   - **Legal basis**: Strictly necessary cookies typically do
     not require consent.
7. **Basic server/access logs**

   - Minimal access logs (including IPs) may be processed for security and
     debugging; we aim to keep these ephemeral or short-retention.

### 4. How we use your data

- **Provide website services**: Secure login (password and/or OAuth),
  maintain sessions, support 2FA, link/unlink providers, associate plugin pages
  with your account, and display analytics.
- **Security and reliability**: Detect abuse, rate-limit requests,
  protect our infrastructure, and troubleshoot issues. Limited, role-based staff
  may review session IP/user-agent data for security.
- **Transactional communications**: If you provide an email, we may
  send verification, password reset, or security notices. We do not send marketing
  emails. Email is optional.

### 5. Third-party processing, subprocessors, and international transfers

- **Account management software**: We operate authentication and
  account features on our own infrastructure. Your account data remains in our
  databases.
- **OAuth identity providers (if you choose to link)**: For example,
  GitHub or Google. We receive your provider identifier and tokens necessary for
  sign-in and store them to maintain your login. You can revoke access via bStats
  or your provider settings. Your provider's privacy policy applies to their
  processing.
- **Hosting**: Our site and data are hosted by [GameHosting.it](https://www.gamehosting.it/).
- **Cloudflare**: Used for content delivery and protection; processes
  IP addresses and related connection data and may set strictly necessary cookies.
- **Email delivery (if email is used)**: We send verification and
  security emails using Amazon Simple Email Service (*Amazon SES*, part of
  Amazon Web Services). When emails are sent, your **email address**, **message content**, and related **metadata** (e.g.,
  recipient, sender, subject, timestamps) are processed by AWS to deliver the
  message and handle bounces/complaints. We configure SES for minimal retention
  and use suppression lists only to improve deliverability. Emails are processed
  by SES in the AWS region(s) we configure; depending on your location, this may
  involve international data transfers. **Providing an email is optional**; you may remove it at any time
  (via account settings or by contacting us).
- **International transfers**: Where applicable, we rely on adequacy
  decisions or recognized frameworks, the EU 2021 Standard Contractual Clauses,
  and, for the UK, the UK Addendum/IDTA. We conduct transfer risk assessments and
  apply encryption, access controls, and minimization.

### 6. Data retention and deletion

- **Account data**: Your profile (display name, username, optional
  email, optional image) and account state (role, ban status) remain until you
  delete your account. Deleted data is removed from active systems promptly and
  purged from backups over our regular rotation cycle.
- **Sessions**: Kept until the session `expires` or you sign
  out; stale sessions are routinely purged. Associated session IP/user-agent are stored
  as part of the session record.
- **Linked accounts/tokens**: Retained until you unlink the provider
  or your account is deleted.
- **2FA secrets/backup codes**: Retained until you disable 2FA or
  regenerate codes.
- **Access/security logs**: Retained for short periods consistent
  with operational security and provider policies; configured to the shortest
  practical duration.

### 7. Security measures

- **Password protection**: Hashing and salting (see Section 3).
- **2FA material**: 2FA secrets and backup codes are stored securely
  (hashed and/or encrypted) and used only for authentication.
- **Encryption**: Data in transit is encrypted via HTTPS; session
  tokens are stored in secure, HttpOnly cookies.
- **Access control**: Only authorized personnel can manage the
  website's infrastructure and stored data; security incidents are investigated
  and, where legally required, we notify users/regulators.

### 8. Your rights (GDPR, UK GDPR, and similar laws)

Depending on your jurisdiction, you may have the right to access, rectify, erase,
restrict, or object to processing, as well as data portability and the right to
lodge a complaint with a supervisory authority. Where we rely on legitimate
interests, you may object at any time.

We respond to verified requests within one month (extendable as permitted).

### 9. California privacy disclosures (CPRA/CCPA)

- **Categories collected**: Identifiers (user ID, username; optional
  email; provider/account identifiers); online identifiers (session token);
  Internet/technical information (IP address, user agent); profile information
  (display name, optional image); account status (role, ban status).
- **Sensitive personal information**: Account login credentials
  (hashed password) and 2FA material (secret/backup codes). Used only to provide
  secure authentication; not used to infer characteristics.
- **Purposes**: Account provision, security/anti-abuse, and
  operational analytics.
- **Sale/sharing**: We do not sell or share personal information
  (as defined) and do not engage in cross-context behavioral advertising.
- **Rights**: Access, deletion, correction, and portability. We
  verify requests (e.g., by account login or request metadata) and respond within
  45 days (extendable as allowed).

### 10. Children's privacy

bStats does not knowingly collect personal data from children under the age of 13
(or 16 in certain jurisdictions). The service is generally aimed at adult server
owners and plugin developers. If you believe a minor's data was submitted, please
contact us at **а​t​n​ос​t​а​] ​t​сѕb ​[ѕ​​t​аt​[t​​о​d​]g​r​​о​**.

### 11. Data protection officer / EU/UK representative

- We currently do not have a Data Protection Officer (DPO). If your jurisdiction
  requires a designated representative or DPO, please contact us at **а​t​n​ос​t​а​] ​t​сѕb ​[ѕ​​t​аt​[t​​о​d​]g​r​​о​** for more information.
- If we are required to appoint an EU/UK representative under Art. 27, we will
  update this policy accordingly and publish the representative's contact details.

### 12. Law enforcement and legal requests

We may preserve and disclose information if required by law or where we believe in
good faith that it is necessary to comply with legal obligations, respond to lawful
requests, or protect the rights, property, or safety of bStats, our users, or the
public.

### 13. Changes to this website privacy policy

We may update this policy as needed—for example, to reflect legal changes or
evolving service features. We will post updated texts on our site with a revised
"Last updated" date.

### 14. How to contact us

For questions, concerns, or requests related to privacy on bStats.org: **а​t​n​ос​t​а​] ​t​сѕb ​[ѕ​​t​аt​[t​​о​d​]g​r​​о​**
