Introduction
_Authentication_ is the process of verifying the identity of a user or entity attempting to access a system or application. Robust authentication is an essential and fundamental aspect of building secure cloud applications, establishing trust between the user and the application. Applications that don’t use authentication will not know who is using the application so will have little basis for restricting actions or holding users accountable.
The value of authentication
There are many benefits to using authentication for applications, including:

- Gatekeeping: Authentication allows apps to verify user identities, ensuring that only legitimate users can access to the application, specific features, and data, protecting against unauthorized usage.
- Enhanced data security: Authentication strengthens application security by enabling the prevention of unauthorized access to sensitive data, reducing the risk of sensitive data disclosure.
- Reduced fraud and abuse: Authentication can help to prevent fraud and abuse by requiring users to identify themselves before they can perform sensitive operations such as making a purchase or accessing data or resources.
- Regulatory compliance: Many industries and jurisdictions have specific regulations and compliance requirements regarding user data protection, recordkeeping, and more. Adequate authentication is a fundamental requirement for [PCI DDS](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard), [HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html), [GLBA](https://www.ftc.gov/business-guidance/privacy-security/gramm-leach-bliley-act), [SOX](https://en.wikipedia.org/wiki/Sarbanes%E2%80%93Oxley_Act), [SOC2](https://en.wikipedia.org/wiki/System_and_Organization_Controls), and others. By having it, you can meet your own business’s compliance requirements and those of potential customers.
  MFA and 2FA
  _Multi-factor authentication_ (MFA) adds additional layer(s) of security by requiring users to provide more than one form of authentication to gain access. The factors are broken down as\[[1](https://www.nist.gov/itl/smallbusinesscyber/guidance-topic/multi-factor-authentication)]:

1.  Something the user knows (such as a password).
2.  Something they have (such as a security token).
3.  Something they are (a fingerprint or other biometric factor).
    MFA is mainly used to strengthen password-based authentication by requiring a different type of factor. It enhances security by making it more difficult for attackers to gain unauthorized access. The essential element is that the additional factor would not be easily stolen at the same time – the attackers would need to compromise both the user's password and the user's additional factor(s) to gain access. MFA is sometimes called _two-factor authentication_ (2FA) when only one additional factor is required.

Approaches to authentication
Multiple techniques are employed for authentication, sometimes in combination for MFA. These techniques encompass:

- [Password-based](/securebydesign/authn-using-passwords/): Here, authentication is based on user-entered credentials - frequently a username and password.
- [WebAuthn](/securebydesign/authn-using-webauthn/): A new standard for web-based authentication that is not reliant on passwords; instead cryptography and secure storage of keys prove that the same user that registered is later authenticating. Passwordless authentication is more secure than passwords and can be easier to use.
- [Passkeys](/securebydesign/authn-using-passkeys/): A new, consumer-oriented, standard for passwordless authentication that several major tech companies are advocating. Based on WebAuthn, [FIDO](https://fidoalliance.org/) passkeys use a cryptographic key pair to authenticate users without the need for passwords.
- [Social login](/securebydesign/authn-using-oidc/): [OpenID Connect (OIDC)](/securebydesign/authn-using-oidc/) is a protocol that allows users to sign into a system or service using their credentials from a social media platform, such as Facebook or Google, making it easier for users to sign into systems and services.
- [Single Sign On (SSO)](/securebydesign/authn-using-saml2/) is achieved when a user is able to authenticate one time using a single identity provider and have that used across a set of systems. This streamlines access. [SAML2](/securebydesign/authn-using-saml2/) is commonly used to achieve SSO.
- [Magic links](/securebydesign/authn-using-magic-links/): Authentication where a user follows a hyperlink that has been sent to them via an email or SMS message; the proof of who the user is lies in their access to the message.
- [Email, SMS, push notification, and voice call authentication codes](/securebydesign/authn-using-trx-otp/): Similar in concept to magic links, but instead of clicking on a link, the user needs to enter a code that was transmitted to them.
- [Time-based One-Time Password](/securebydesign/authn-using-totp/) (TOTP): A type of two-factor authentication that uses a temporarily valid randomly generated code. TOTP is often used in conjunction with passwords to provide a more secure authentication experience.
- [Biometric-based authentication](/securebydesign/authn-using-biometrics/): authentication based on unique physical characteristics of a user such as their fingerprint or face.
  Applications sometimes support multiple authentication approaches to meet the needs of different users.
  Quick notes
- Applications can build their own authentication system (which can be complex especially if it needs to be flexible) or use a third-party authentication provider.
- To achieve gatekeeping, an application needs to make an authorization\[[2](https://en.wikipedia.org/wiki/Authorization)] decision at the time of an operation or access by the user. Authorization decisions are either hard-coded or based on an authorization engine evaluating a defined policy.
- Both successful and failed authorization attempts should be recorded in your audit log\[[3](https://pangea.cloud/securebydesign/secure-audit-logging-overview/)].
