[[Web-Service-Security]]

##### Challenges and Threats to Web Service Security

Since they represent **a messaging and abstract interfacing layer**, Web services cannot (and should not) exploit some of the security mechanisms used by the underlying platforms on which the web services run.

> Hence, operating system-level protections such a file or device protection, memory protection or network level protection should not be replicated in the web services environment.

Generally, security solutions should be implemented via the **transport layer**, the **Web services layer** and the **data layer** to establish stronger protection against the ever-increasing threats and challenges.

##### The Expectation

In the domain of web services the security solutions should be mapped into and out of the underlying execution environment to ensure the following:

-   Enforcement of the security policy defined.
-   When the assurance to security policy cannot be properly defined: the proper maintenance of an audit log which contains entries of the failure or policy breach

##### Message Interception

The possibility of intercepting and decoding SOAP messages draws in security threats that must be defended against when deploying Web services.

Web services messages are usually transmitted as plain text, which can easily be intercepted and read (Unless they are specifically encrypted).

##### Message Interception: The Threats

Message interception provokes the following threats:

-   **Content modification** which could affect all or part of the message body/headers.
-   **Addition of bogus information** into the message body/headers.
-   **Modification/Alteration** of message attachments.
-   **Unauthorized access** to confidential, sensitive information.

> Use of **encryption** techniques and **digital signatures** can help tackle threats against message interception thus ensuring **confidentiality and integrity**.

##### Person in the Middle Attacks

SOAP messages can be routed through intermediaries and intermediaries have the access rights to examine the messages to process headers.

Compromised intermediaries pose a severe threat to WS Security, as the communication between the end-users can be intercepted without their knowledge.

> **Mutual authentication** techniques provide a solution to this type of threat.
> 
> **Signed keys** or **derived keys** further enhance the protection.

##### Spoofing

Spoofing poses additional challenges to security as the attacker presumes the identity of a trusted/authenticated entity to bypass the security system.

Spoofing aims at deceiving the target to believe the authenticity of the communicating entity.

Spoofing usually opens the door to usher in other forms of attacks such as message forgery.

> **Mutual authentication** techniques can be exploited as a solution against this type of threat.

##### Replay Attacks

In a replay attack, a malicious attacker intercepts a message and replays it back to the receiver.

Replay attacks could be exploited to invoke fraudulent transactions or to collect confidential information

> **Strong authentication techniques** along with **message time stamp** and **sequence numbering** as a shield against this type of threat.

##### Denial-of-Service Attacks

Unauthorized attackers or intermediaries who manage to intercept a SOAP message successfully can provoke a denial of service attack by repeatedly resending it to overload the web service execution environment.

-   Such a scenario could cause services to be denied to legitimate services/users.

An attacker who manages to get hold of the address can also blast a ton of messages to the web service to interrupt services.

Even if the messages are rejected, the site can get overloaded with error processing.

##### XML Bomb

[Technopedia](https://www.techopedia.com/definition/13716/xml-bomb) defines XML Bomb as

> _An XML bomb is a piece of XML code that is syntactically valid and correct but can cause a program that compiles or runs it to crash or hang._

The security level of a server can be tested using XML Bomb.

-   Within an HTML code, an XML code is either parsed internally or referenced as an external file that is directed to a server.
    
-   Basically, a typical server without enough protection is expected to crash with this attack.
    

An XML bomb exploits three properties of XML: **entity substitution**, **nested entities** and **inline DTDs**, which results in **"data explosion"**. Hence the "bomb" in the name

##### Understanding the Security Architecture

It is vital to examine the security challenges and threats to web services within their overall architectural background and analyze solutions based not simply on a particular technology but also by reviewing the overall solution context.

> That is, you cannot just say “use SSL” without having a sound understanding of the threat you are trying to handle and without understanding the overall security setting into which you would like to deploy SSL.
> 
> `SSL may be sufficient, but it may not.`

Heterogeneous security solutions must often be used simultaneously in order to extend a comprehensive solution to the prominent security concerns, and hence it is crucial to understand how the technologies work together.