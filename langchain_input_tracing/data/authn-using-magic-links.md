Overview
Magic link authentication is a passwordless [user authentication](/securebydesign/authn-intro/#value-of-authn) method that sends a single-use link to the user’s email address (or, less commonly, via SMS) to verify their identity. When the user clicks on the link, they are automatically (“magically”) logged in to the application (or there may be additional login steps that follow).
It can be used by itself for a potentially fully passwordless experience, for cases in which it provides an adequate level of security. More commonly though, it is used for [multi-factor authentication](/securebydesign/authn-intro/#mfa-and-2fa) (MFA), for example on top of [password-based authentication](/securebydesign/authn-using-passwords/), providing an additional layer of security. In terms of MFA, magic links are considered a “something the user has” factor since it proves the user has access to their email account – the presumption being that they are the only ones with access.
As a form of authentication, magic link authentication [provides](/securebydesign/authn-intro/#value-of-authn) gatekeeping, enhanced data security, and reduced abuse to your app. Having robust authentication bolsters the security of your application, builds trust with users by demonstrating a commitment to protecting their data, helps to safeguard your reputation, and can facilitate adherence to compliance standards. Magic links can provide strong authentication and do so in a way that is convenient for users. No standards govern magic link authentication. Each application can implement it in its own unique way, resulting in various variations and approaches and a lack of interoperability.
Magic link authentication
A dive into magic link authentication
This diagram presents an overview of the magic link authentication process:

As shown, the active entities involved in magic link authentication are:

- The user that needs to authenticate.
- The application the user is attempting to access. This must include a website.
- An email relay, used to transmit the magic link email.
- The user’s email service.
  When initializing a user session, the application will construct a unique URL. The initial elements of the URL correspond to the web server being used and specifically the handling logic for magic links. The URL contains a direct or indirect reference to the user (or the specific user session ID, if session initiation has begun). The session’s persistent state is updated with the specific details of the URL.
  The URL is then sent via email to the user. Once they receive it, they click on the hyperlink and it opens on the device they were viewing the email on. That causes the URL to be received by the magic link handling endpoint, which checks if the URL is valid and matches a magic link that was sent out. If it does, magic link authentication has succeeded for that session and the user may be logged in for that session. If there is no match to a valid transmitted magic link, no user session is established (see [below](#higher-security-implementation) for some best practices for this situation).
  This authentication mechanism is similar to how emails supporting email address verification or account recovery operate, though those are for different situations. Magic link authentication is also similar to [emailed one-time passcode (OTP) authentication](/securebydesign/authn-using-trx-otp/), but a URL is transmitted instead of an OTP and the user clicks on the URL rather than personally viewing and entering a code.
  Diving deeper
  To add magic link authentication to their app, developers will need to use a third-party authentication provider or build their own magic link authentication system.
  Typically, clicking the URL opens a new tab for the user and that is where the established authenticated session is located. The magic link handler could instead have the original browser tab become logged on. This is especially valuable for cases such as where:
- Users use your app on one device (such as a laptop) and read their email on a different device (such as their mobile phone).
- They use a different browser for reading email.
- They use your app in a browser or browser profile different from the one email links open to.

In such cases, without this special handling, the authenticated session could be in a suboptimal or incompatible location.
Often you will want to recognize the user as the same person across different sessions, so you will have an account database, holding information collected during user registration. This may be updated over time. To help protect against spamming and typos, you will likely want to verify the email address provided by the user.
Enhancing the security of magic links authentication
The strength of authentication offered by magic link authentication and imparted on your application depends on (1) the security of the user’s email account and (2) the application’s magic link implementation choices.
Raising the security of the user’s email account
You should inform and remind users that their email security may be the weakest security link. Encourage (and require if possible) the user to follow strong security practices for their email account such as requiring strong [authentication](/securebydesign/authn-intro/) on the account, such as by using a hard-to-guess unique password plus 2FA or using FIDO passkeys or WebAuth. Also, educate them about phishing.
Higher security from your magic link implementation
Consider following these practices for improved security:

- If an attacker can predict (either specifically or with enough guesses) the emailed URL, then they need not even hack into the user’s email. That means that the unique part of the URL should be both long and hard to predict. A quality random number generator is the most reliable way to make it hard to predict.
- Reduce attackers’ opportunities by:
  - Only allowing a magic link URL to be used for authentication a single time. (Note that security software might automatically visit URLs in incoming emails, so you may need to disregard that case perhaps by confirming intent to log in.)
  - Limiting the number of attempts to complete magic link authentication for a session — perhaps to one since that is all it should take.
  - Having the magic link validity period be as short as practical.
  - Implementing concurrency or rate limits on the session initiations for a user. Remember, attackers may make many attempts to log in as the user, resulting in more simultaneously valid magic links that can be guessed or intercepted.
- Make it easier for a user to recognize genuine magic link emails so they will be less likely to fall for phishing. Use best practices\[[1](https://sendgrid.com/blog/10-tips-to-keep-email-out-of-the-spam-folder/)] to make it harder for phishers to trick your users.
- Maintain tight security on your magic link creation and transmission processes and your session storage.
- For better security and privacy, it is best to not include any potentially recognizable or guessable information in the magic link URL itself. A random nonce is better than even a keyed cryptographic hash of authentication data.
- [Audit log](/securebydesign/secure-audit-logging-overview/) both successful and unsuccessful attempts to authenticate using magic links as well as all magic links generated. For failures, log the reason (e.g., expired URL vs. URL was never sent out). Investigate failures. Invalid magic links may signal an attack; review the audit log for context.
- Employ secure coding best practices\[[2](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/stable-en/)], noting that the magic link handling logic may face malicious URLs.
  Benefits and considerations for supporting magic link authentication in your app
  Benefits from supporting magic link authentication in your app include:
- Magic links can be easily added as 2FA, adding a beneficial layer of security on top of approaches with security problems such as [passwords](/securebydesign/authn-using-passwords/) (guessing/disclosure/phishing/etc.). Magic links provide a higher level of security than email-based OTP authentication for multi-factor authentication (MFA) because they are less vulnerable to guessing. Nevertheless, their robustness may not be as high as that of [TOTP](/securebydesign/authn-using-totp/) (Time-based One-Time Password) authentication, primarily due to their reliance on strong security on the user's email account.
- Authentication with magic links is streamlined and does not rely on the user remembering anything or having to type in a password or OTP. Thus friction is fairly low and it can be more convenient for users, especially on mobile devices.
- Magic links can be used to simplify the onboarding process by eliminating the need for users to create and remember passwords. This approach reduces friction during initial registration and encourages user engagement. It can also benefit users who are overwhelmed by passwords or have problems remembering them.
- Email is familiar to users and it is inexpensive to send an email.
- Since magic links should be time-limited and single-use, the risk of unauthorized access due to credentials that are stolen from the application backend, on the user side, or intercepted in transit is significantly reduced.
  Consider though:
- Compared to magic links as the sole authentication factor, [FIDO passkeys](/securebydesign/authn-using-passkeys/) and [WebAuthn](/securebydesign/authn-using-webauthn/) provide stronger security and are also user-friendly, though users may be less familiar with those.
- Email can be slow to show up in the user’s email client for various reasons, leaving the user and your app waiting and users may abandon logging in or decide to start over. The magic link email may be hit by a spam filter. These may make it poorly suited for some use cases.
- Users may be understandably wary of clicking on links in emails due to being educated on security, so you may need to take extra steps to instill them with confidence\[[3](https://security.ucop.edu/resources/create-less-phishy-emails.html)].
- Account recovery – You will need a process in place for users who can’t access their email or encounter issues with magic link delivery. Offer account recovery options (possibly involving a secondary email or a phone number) that maintain appropriate security.
