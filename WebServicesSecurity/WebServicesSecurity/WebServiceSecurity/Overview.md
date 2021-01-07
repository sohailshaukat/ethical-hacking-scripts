##### Web Security Testing

It usually takes more than using a tool in WSDL to analyze security issues to precisely test a Web service. However, not much effort and time has been invested in this area by the security communities.

The traditionally exploited testing techniques and testing methodologies may not be efficient enough to handle the ever-increasing real-world threats and vulnerabilities facing Web services.

Lack of proper testing environments, tester expertise and practical solutions to testing makes the testing process challenging.

##### OWASP Web Service Testing Methodology

The OWASP testing guide v4 elucidates techniques for testing Web services. They are as follows:

-   **WS Information Gathering** – The WS entry point, as well as the communication schema are determined
    
-   **Testing WSDL** – Testing the WSDL can be done once the WS entry point is determined.
    
-   **XML structure Testing** – If the XML is not well-formed, it will fail once parsed on the server side. The structure of the XML needs to be tested to make sure that it runs the entire XML message from top to bottom in a serial way to ensure that the XML is well-formed.

-   **XML Content Level Testing** – Typically the content-level attacks target the server that hosts a web service and any applications which are used by the service.
    
-   **HTTP GET Parameters / REST Testing** – Several XML applications are raised by sending them as parameters through HTTP GET queries. Attackers can pass malicious content through the HTTP GET string to attack the web services.
    
-   **Naughty SOAP Attachments** – Various risks are involved in processing the server attachments and redeploying the file to the clients. This section tests the attack vectors for Web servers that accept attachments.

##### Penetration Testing of Web Services

The penetration testing of Web services demands the following as prerequisites:

-   **Sample API file** ( WSDL/ SOAP, etc.)
-   **Sample request/ response** ( to understand the values and data exchanged)
-   **Entry points/ URLs**

##### WS Penetration Testing: Tools

The following tools may be exploited to perform Web services penetration testing:

-   Fiddler
-   Burp Suite
-   Acunetix/IBM Security AppScan
-   ZAP Proxy
-   Curl
-   SOAP UI

##### Testing Methodology

### Automated Testing Tools

-   SoapUI Pro
-   OWASP ZAP
-   HP Webinspect
-   BM AppScan
-   WSMap
-   WSBang

### Manual Testing Tools

-   Soap UI Free
-   Burp Suite Pro
-   Postman ( with Burp)

##### Testing Methodology

### Extensions

-   SAML Editor
-   SAML Encoder / Decoder
-   WSDL Wizard
-   Wsdler
-   SOA Client

##### Test Cases to Find in Web Services

• Fuzzing • XSS /SQLi/ Malformed XML

• File Upload • Xpath Injection

• XML Bomb (DoS) • Authentication based attacks

• Replay attacks • Session fixation

• XML Signature wrapping • Session timeout

• Host Cipher Support/ Valid Certificate/ Protocol Support

• Hashing Algorithm Support

##### Takeaways

-   [Web Service Security Testing Cheat Sheat](https://cheatsheetseries.owasp.org/cheatsheets/Web_Service_Security_Cheat_Sheet.html)
-   [Testing WSDL](https://www.owasp.org/index.php/Testing_WSDL_(OWASP-WS-002))
-   [SoapUI](https://www.soapui.org/soapui-projects/soapui-projects.html)