##### What is a Web Service?

In association with W3C Web Services, the W3C has defined a web service as follows:

> -   _A web service is a software system designed to support **interoperable machine-to-machine interaction** over a network._
>     
> -   _It has an interface described in a **machine-processable format** (specifically WSDL)._
>     
> -   _Other systems interact with the web service in a manner prescribed by its description using **SOAP messages**, typically conveyed **using HTTP with an XML serialization** in conjunction with other web-related standards._

##### In a Nutshell

In short, a web service can be described as a service that:

-   Is available over the Internet or private networks
-   Makes use of a standardized XML messaging system
-   Is platform and language independent
-   Is self-describing through a common XML grammar
-   Is discoverable through a simple find process.

##### Characteristics of Web Services

-   XML-Based
-   Loosely Coupled
-   Coarse-Grained
-   Ability to be Synchronous or Asynchronous
-   Supports Remote Procedure Calls (RPCs)
-   Supports Document Exchange

##### Components of a Web Service

Over the past few years, the following primary technologies have emerged as worldwide standards that make up the core of today's web services technology.

-   **XML-RPC**
-   **SOAP** (Simple Object Access Protocol)
-   **UDDI** (Universal Description, Discovery, and Integration)
-   **WSDL** (Web Services Description Language)

##### XML-RPC

-   The simplest XML-based protocol for exchanging information between computers.
    
-   Requests are encoded in **XML** and sent via **HTTP POST**.
    
-   XML responses are embedded in the body of the **HTTP response**.
    
-   Platform-independent.
    
-   Allows diverse applications to communicate.
    
    -   A Java client can speak XML-RPC to a Perl server.

##### SOAP

-   SOAP stands for **Simple Object Access Protocol**.
    
-   It is an **XML-based protoco**l for accessing web services.
    
-   A W3C recommendation for communication between applications.
    
-   Is XML based, so it is **platform independent and language independent**.

##### WSDL

-   WSDL stands for **Web Services Description Language**.
-   It was developed jointly by Microsoft and IBM.
-   It is the **standard format for describing a web service**.
-   Basically, **an XML document** containing information about web services such as method name, method parameter and access information.
-   An XML based protocol for exchanging information in distributed and decentralized environments.
-   WSDL **is a part of UDDI** and acts as an interface between web service applications.

##### UDDI

-   UDDI stands for **Universal Description, Discovery, and Integration**.
    
-   An **XML based** framework for **describing, discovering and integrating web services**.
    
-   A directory of web service interfaces described by WSDL, containing information about web services.
    
-   An **open industry initiativ**e allowing businesses to find and explore each other and define how they interact over the Internet.

##### Web Service Architecture

#### Web Service - Roles

There are three major roles within the web service architecture.

-   **Service Provider**
    
    -   The provider of the web service: Implements the service and makes it available on the Internet.
-   **Service Requestor**
    
    -   Any consumer of the web service: utilizes an existing web service by opening a network connection and sending an XML request.
-   **Service Registry**
    
    -   A logically centralized directory of services.
    -   The registry lays out a central place where developers can publish new services or find existing ones.

##### Web Service Architecture

#### Web Service - Roles

There are three major roles within the web service architecture.

-   **Service Provider**
    
    -   The provider of the web service: Implements the service and makes it available on the Internet.
-   **Service Requestor**
    
    -   Any consumer of the web service: utilizes an existing web service by opening a network connection and sending an XML request.
-   **Service Registry**
    
    -   A logically centralized directory of services.
    -   The registry lays out a central place where developers can publish new services or find existing ones.

##### Web Service Roles: An illustration

![[22113_Web_Service_Roles.jpeg]]

##### Web Service Protocol Stack

[Youtube](https://youtu.be/u80uPzhFYvc)

The web service protocol stack provides a window for illustrating the web service architecture. At present, the stack has four main layers:

-   **Service Transport**: Handles the transportation of messages among applications.
    
    -   Currently, this layer includes HyperText Transport Protocol (HTTP), Simple Mail Transfer Protocol (SMTP), File Transfer Protocol (FTP), and Blocks Extensible Exchange Protocol (BEEP).
-   **XML Messaging**: Facilitates the encoding of messages in a common XML format so that messages can be comprehended at either end.
    
    -   Currently, this layer includes XML-RPC and SOAP.

-   **Service Description**: Facilitates the description of a public interface to a specific web service.
    
    -   Web Service Description Language (WSDL) handles service description.
-   **Service Discovery**: Centralizes services into a common registry and provides easy publish/find functionality.
    
    -   Universal Description, Discovery, and Integration (UDDI) handles service discovery.
