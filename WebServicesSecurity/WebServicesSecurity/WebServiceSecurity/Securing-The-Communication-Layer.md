[[Web-Service-Security]]

##### Securing the Communication Layer

The communications transport layer is the first level that needs to be secured. In the domain of Web Services, it is almost always **TCP/IP**, and this is the case when **HTTP** is used.

**Firewalls** prevent access by programs at unauthorized addresses by mapping a publicly known IP address to a different IP address on the internal network, hence establishing a managed tunnel.

Web services can handle existing firewall configurations, which most often implies that improved protection has to be included in firewalls to analyze incoming SOAP traffic and log any problems.

Another prominent solution involves the exploitation of **XML firewalls and gateways** that are efficient in recognizing Web services formats and conducting initial security checks.


##### IP Layer Security

Security methods for the Internet include the **IP layer with IP security (IPsec)**.

IPsec presents **packet-level encryption** and **authentication** and is usually implemented at the operating system level.

IPsec is a provision accessible to all applications using the Internet, including Web services.

However, this implies that the IPsec connection is a part of a separate security setup between the communicating entities.

Notably, for Web services to use IPsec, the IPsec communication session has to be established before invoking a Web service, typically by the user or the transport, since nothing in the Web services layer can be used to establish an IPsec session.

##### IP Layer Security

IPsec is most often used in **Virtual Private Network (VPN)** applications and between firewalls, which many companies exploit to secure the communications between corporate systems and remote users.

Other VPN technologies are also widely adopted as a foundation for security in Web services invocations, just the way they are used by any other Internet-based application.

##### Transport Layer Security

The next level to be considered is transport layer security.

Typically, this is ensured by **Secure Sockets Layer/Transport Layer Security**(SSL/TLS, commonly referred as SSL), which is often seen on the Web as **HTTPS**.

This security level can be enforced in the network application, and Web services can directly and easily exploit it by choosing HTTPS as a transport.

Implementations of SSL for other transports, such as **IIOP** and **RMI/IIOP**, also present the potential for Web services to exploit this important privacy mechanism when employed over other transports.

##### SSL/TLS
[Youtube](https://youtu.be/sEkw8ZcxtFk)

##### SSL in WS-Security: The Pros

-   SSL provides **encryption and strong authentication** and may be enough for many applications.
    
-   SSL authentication can be exploited to provide **strong, mutual authentication** - much stronger than HTTP Basic, HTTP Digest, or WS-Security username token authentication


##### SSL in WS-Security: The Cons

-   SSL is **transport-based rather than application-based**, and hence secures the network nodes instead of the service requester or provider.
    
-   SSL provides **message confidentiality**, **authentication**, and **message integrity**, but these capabilities are restricted to the transport level, and **cannot be extended to the application level**.
    
-   SSL also does not provide any protection for **XML data** in storage.
    
-   It does not provide direct support for any of the advanced authorization checks such as **role-based authorization** that may be required by many applications.
    
    -   However, it is possible to map the SSL strong authentication information to a local principal and use that in an application-defined role-based authorization scheme to determine access privileges.

##### Transport Layer Security: Authentication

Basic authentication techniques (such as basic username/password), may not be sufficient for Web Services.

Passwords could be encoded using **Base64** or some simple **obfuscation algorithm** even without SSL.

-   However, obfuscation does not provide true encryption and hence is not very secure.
-   If a potential attacker figures out the algorithm or encoding mechanism used for the obfuscation, the message can easily be compromised.

Additional, stronger authentication mechanisms include:

-   At the transport level: **HTTP Basic**, **HTTP Digest**, and **SSL**.
-   At the application level: **Username/password**, **X.509**, **Kerberos**, **SPKM**, **SAML**, and **XrML**.

