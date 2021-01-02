[[Web-Services]]
##### The Overarching Concern

> Security is considered to be an **overarching concern** because almost everything in the digital world demands some protection from the ever - increasing threats and challenges at some point in time.

For example, in the domain of web services

-   The security of SOAP messages need to be ensured
-   WSDL files may have to be protected against unauthorized access
-   Firewall ports may require strategies to handle heavy loads and monitor web service messages, and so on.

Since **interoperability** is a key characteristic of web services, while security mechanisms are added to web services it has to be ensured that the **execution environment technologies remain operational.**	

##### Web Service Security

[Technopedia](https://www.techopedia.com/definition/24385/web-services-security-ws-security) defines Web Service Security as:

> _**Web Services Security (WS Security)** is a specification that defines how security measures are implemented in web services to protect them from external attacks._
> 
> _It is a set of protocols that **ensure security for SOAP-based messages** by implementing the principles of **confidentiality**, **integrity**, and **authentication**._

There are three specific security issues with web services:

-   **Confidentiality**
-   **Authentication**
-   **Network Security**

##### Confidentiality

_**How can confidentiality be ensured when a client sends an XML request to a server?**_

The answer lies in the points below.

-   **XML-RPC** and **SOAP** primarily run on top of **HTTP**.
-   HTTP supports **Secure Sockets Layer (SSL)**.
-   SSL can be used to secure communication.
-   SSL is a widely deployed proven technology.

##### Challenges to Confidentiality

A chain of applications may be associated with a single web service.

-   For instance, The services of three applications may be tied together by a single large service.
    -   In such a scenario, SSL may not be adequate and the messages will have to be encrypted at each node in the service path. Hence each node acts as a potential weak link in the chain.
    -   One promising provision to the issue is the **W3C XML Encryption Standard**.
        -   The W3C XML Encryption Standard provides a framework for encryption and decryption of XML documents.

##### Authentication

_**How can a user who connects to a web service be identified? Is the user authorized to use the service?**_

The following options can be considered but there is no clear consensus on a strong authentication scheme.

Though there is no coherent consensus on a secure authentication scheme, the following points may be considered.

-   Services can be protected in a similar manner as HTML documents are currently protected since HTTP encompasses in-built support for **Basic and Digest authentication**.
    
-   **SOAP Digital Signatures** exploits public key cryptography to digitally sign SOAP messages enabling clients/server to authenticate the identity of the end user.

##### Network Security

Network security has been the subject of speculation with no easy solutions to the problem.

To filter out SOAP or XML-RPC messages:

-   One option is to filter out all HTTP POST requests that set their content type to text/XML.
    
-   Another possibility is to **filter the SOAPAction HTTP header attribute**.
    

**Wireshark** and **Fiddler** are tools that can be used to monitor HTTP traffic.

##### WS Security: Core Concepts

Two basic security mechanisms are employed by web services to handle security risks:

-   **Signing**
-   **Encrypting Messages**

These mechanisms are used to ensure data integrity, confidentiality, checking token and ticket information to set the seal on authentication and authorization.

These mechanisms are usually incorporated in combination to handle various aspects of security as a broader picture of risks needs to be analyzed to tackle them efficiently.

##### WS Security Headers

![[22124_Security_Headers.jpeg]]

WS-Security headers, which may include mechanisms for **authorization**, **authentication**, **encryption**, and **signature** can be added to SOAP messages enabling service providers to verify the credentials of the service requester.

Authentication and authorization information from the requester is usually represented in the form of **tokens**.

Hence, efficient strategies to communicate and coordinate security information(tokens) between communicating parties need to be enforced.

##### WS Security: Encryption

Before a message is transmitted, an encryption algorithm can be used to encrypt the messages. The encrypted message can then be decrypted at the receiver's side before processing.

> Encryption is the process of transforming data into an unintelligible form so that an unauthorized person cannot make sense of the underlying message.

Encryption enhances the security-related with **authentication and authorization** of data (such as a password), even if the content of the SOAP body isn't encrypted.

The details of encryption such as the algorithm used may be embedded in the **WS Security header.**

##### WS Security: Encryption

![[22126_WS_Security_Encryption.jpeg]]

Other extended technologies, such as **reliable transactions and messaging** may be used in combination with the basic security mechanisms to enhance the security of the overall system.

Additional messages may be required by transaction processing technologies to facilitate coordination among transaction protocols which demand security to deter disruption.

##### WS Security: Identity Management

The identity of a web service requester is crucial in **establishing trust between the web service requester and provider** since access controls for services, resources. Alternatively, devices are based on the identity of the requester.

Since web services can span across departments and enterprises, managing identity for web services can be a complex task.

> Identity management can be performed locally, departmentally, or within an organization.
> 
> Sometimes identity management will have to be performed under a broader scope, such as a **corporate-wide LDAP solution** or the **Microsoft Active Directory.**

When identities have to be precisely managed across the Internet or enterprises, the need for trust increases so does the level of administrative difficulty.

##### WS Security: Authentication

Web service requesters can incorporate authentication information using **username-password information** in SOAP headers which the service provider can verify against its authorized directory of usernames and passwords.

The username and password information can also be sent through **HTTP without the use of a SOAP header**.

> Further refinement of this model may be carried out by the provider to reinforce authorization checks for access specific services or certain data resources.

Authorization may sometimes be carried out based on specific roles such as admin, manager, or clerk which is typically managed by the service provider.

##### Finding the Right Balance

As with any application, **a sound equilibrium between business requirements, performance, security, and ease of administration** needs to be established even for web services.

Security techniques carry a performance price not only in terms of **additional processing overhead** while executing a service but also to the professionals who design, develop, and administer them.

Encryption encompasses an implicit overhead considering the **time involved** in the process. Incorporation of a username/password on each message further adds to processing overheads.

---

Hence, it is trivial not only to perceive the solutions provided by the technology but also to consider the overhead costs while exploring less expensive but equally efficient solutions.