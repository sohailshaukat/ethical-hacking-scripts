##### Message Level Security

Message-level security is the next level of security above the transport level in which the WS-Security framework and associated specifications provide the security protections.

The **WS-Security framework** defines **SOAP headers** incorporating the necessary information to protect messages.

The **WS-Security specification** defines the security header for SOAP messages and components of the header (including what can be included).

The contents of the SOAP security header and the associated processing rules are defined in the associated specifications.

##### The Challenges

The use of Web services imposes additional challenges to security as Web services exhibit access to programs and data stores.

Moreover, complex Web services may be spread across multiple network locations discovered dynamically or may constitute a larger interaction.

Since sensitive information could be passed from one service to another, Web services require an **end-to-end security model**.

Interactions in a Web service could involve multiple parties using discrete security-related technologies.

##### WS-Security Framework

**WS-Security (Web Services Security)** is the name of a set of specifications that enhances SOAP message headers to integrate solutions to common security threats, particularly those associated with Web services messaging.

#### The major motivation

**WS-Security** must define how **XML Encryption and XML Signature** should be used with **SOAP** as SOAP is a variant of XML documents devised for messaging and interoperability.

#### WS Security Protects Against:

-   **Message alteration**: By including digital signatures for all or parts of the SOAP body and the SOAP header.
-   **Message disclosure**: By supporting message encryption.

##### WS-Security Framework

#### Other Uses

-   Preserves message integrity by exploiting of strong key algorithms.
-   Authenticate messages by exploiting various token mechanisms such as Kerberos and X.509

#### WS-Security Specifications

-   SOAP Message Security.
-   Username Token Profile.
-   X.509 Token Profile.
-   Profiles for the use of other technologies with the framework such as SAML, Kerberos, and XrML

##### WS-SecurityPolicy

**WS-SecurityPolicy** is a policy assertion language that can be used within the **WS-PolicyFramework**

An XML-based assertion associated with a Web service endpoint or WSDL file can be developed with **WS-SecurityPolicy** using **WS-PolicyAttachment**

**WS-SecurityPolicy** association can be discovered by a service requester using the **WS-MetadataExchange protocol**

-   Otherwise, a URL pointing to the XML file in which the WS-SecurityPolicy assertion is stored has to be dereferenced.

Decoding the WS-SecurityPolicy assertion helps the service requester understand the security features that are required by the service provider.

##### WS-SecurityPolicy

**WS-SecurityPolicy** is a policy assertion language that can be used within the **WS-PolicyFramework**

An XML-based assertion associated with a Web service endpoint or WSDL file can be developed with **WS-SecurityPolicy** using **WS-PolicyAttachment**

**WS-SecurityPolicy** association can be discovered by a service requester using the **WS-MetadataExchange protocol**

-   Otherwise, a URL pointing to the XML file in which the WS-SecurityPolicy assertion is stored has to be dereferenced.

Decoding the WS-SecurityPolicy assertion helps the service requester understand the security features that are required by the service provider.

##### WS-Trust

At times, the service provider and requester may have to communicate out of band (i.e., out of the customary Web service invocation message exchange) to interchange security credentials.

For instance, before sending a message, a requester may have to obtain a service provider's public key for encryption.

The **WS-Trust specification** defines a set of rules for evaluating and arbitrating a trusted relationship such as this.

WS-Trust establishes a protocol for:

-   **Issuing, validating and renewing security tokens.**
-   **Evaluating or arbitrating trust relationships.**

WS-Trust defines the process of exchanging and arbitrating security tokens so that the requester can gain the necessary security information to construct trusted messages.

##### WS-Trust

![[22160_Ws_Trust.jpeg]]

As illustrated in the image above WS-Trust elucidates a SOAP message exchange protocol based on which a service requester and provider can communicate with each other to exchange authorization and authentication credentials.

##### WS-Trust

The security model described in **WS-Trust** is based on a process in which a Web service provider can insist that an incoming message from a requester establish a set of credentials (userId/password, permission, key, capability, etc).

**WS-Trust** establishes the message exchange pattern and format of the information credentials that may have to be exchanged between the requester and provider in order to satisfy the policy assertions.

-   Security tokens are requested using the `<RequestSecurityToken>` message described in the WS-Trust specification.
    
-   Security tokens are returned using the `<RequestSecurityTokenResponse>` message described in the WS-Trust specification.

##### WS-SecureConversation

**WS-SecureConversation** elucidates a shared security background across multiple message exchanges.

It defines a new security context background for the `<wsse:Security>` header block, and it describes a binding for WS-Trust.

Instead of having to incorporate the same security credentials in each SOAP message, a provider and requester can use **WS-SecureConversation** to negotiate sharing a common security context.

For example:

```
<SecurityContextToken wsu:Id="...">
   <wsc:Identifier>...</wsc:Identifier>
</SecurityContextToken>
```

##### WS-SecureConversation

![[22163_WS_Secure_Conversation.jpeg]]

As illustrated in the image above, WS-SecureConversation describes a SOAP message protocol for establishing and propagating common copies of security context at the provider and requester nodes.

The shaded areas illustrate shared security context used across multiple message exchanges.

##### WS-Federation

**WS-Federation** describes the process of **establishing trust relationships** across security domains.

WS-Trust presumes a **single security domain** within which the service requester authenticates with the service provider’s authentication service.

WSFederation elucidates a binding of WS-Trust that facilitates a service provider to handle authentication credentials that originate from a different security domain.

> Since Web services can span across multiple domains, problems related to authentication and access control of identities has to be handled for various domains.

The WS-Federation specification illustrates a message exchange protocol that service providers and requesters can employ to establish a federation of security domains spanning multiple trust boundaries.

The Federation of security trust domains can be accomplished by using **WS-Security, WS-PolicyAssertions, and WS-Trust** in combination.

Particularly, WS-Federation takes WS-Trust a step further and initiates a mechanism for **interchanging credentials across trust boundaries**, not just within a trust boundary.

-   Security tokens are requested using the`<RequestSecurityToken>` message described in the WS-Trust specification.
    
-   Security tokens are returned using the `<RequestSecurityTokenResponse>` message described in the WS-Trust specification.

##### SAML

The **Security Assertion Markup Language (SAML)** from OASIS is an XML application that aims to assist single sign-on and propagate authorization information.

> For example, SAML helps a user to log on to a Web site once and then access affiliated Web sites without having to log on again.

The WS-Security SAML profile describes the process of using SAML with SOAP, but SAML can also be used independently of SOAP and WS-Security, if necessary.

To enable single sign-on, SAML defines three basic components: **assertions, protocol, and binding**.

[Youtube](https://youtu.be/gUmMcecHN9s)