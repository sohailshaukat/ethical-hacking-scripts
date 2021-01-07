##### Data Level Security

Two of the fundamental security specifications for ensuring the protection of Web services data are **XML Signature** and **XML Encryption** as Web services specifications are applications of XML.

> For example, WSDL files can be protected against unauthorized access by encryption and WSDL files can be protected against tampering by signing them.

It is particularly important to give a thought to using these XML security technologies when:

-   The XML data has to be protected outside the scope of a SOAP message.
-   When the metadata of Web services need to be protected from unauthorized access.

##### XML Encryption

SSL can be used to encrypt XML payload when carried over HTTP, but at times it might not be enough.

It is vital to have specific strategies for the encryption of XML documents when transmitting XML over other transports, possibly over multiple modes of transport, or while storing XML documents in a database or a file.

During encryption, the `EncryptedData` element described in the XML Encryption specification replaces the content or element in the encrypted version of the XML document.

> Encryption can be nested to any level.

The entire document (except the encryption headers) or any specific element within the document can be encrypted.

##### Selective Encryption

**Selective encryption** can be practically exploited when only a part of a document needs to be encrypted.

Tags, as well as the data contained, can be encrypted to achieve complete confidentiality of information.

> For example, hiding a `<creditcard>` tag inside a `<CipherData>` tag.

##### An Example

```
<?xml version='1.0'?>
   <PaymentInfo xmlns='http://www.iona.com/artix/paymentService'>
      <Name>Eric Newcomer</Name>
      <CreditCard Limit='50,000' Currency='USD'>
         <Number>5555 5555 5555 5555</Number>
         <Issuer>Example Bank</Issuer>
         <Expiration>04/02</Expiration>
      </CreditCard>
   </PaymentInfo>
```

Above is an example of a plain, unencrypted data.

##### The Encrypted Form...

The encrypted form of the data is as follows:

```
<?xml version='1.0'?>
   <PaymentInfo xmlns='http://www.iona.com/artix//paymentService'>
      <Name>Eric Newcomer</Name>
      <EncryptedData Type='http://www.w3.org/2001/04/xmlenc#Element'
         xmlns='http://www.w3.org/2001/04/xmlenc#'>
          <CipherData>
             <CipherValue> A23B45C56...</CipherValue>
          </CipherData>
      </EncryptedData> 
    </PaymentInfo>
```

-   `CipherData` element contains the encrypted data.
-   If an application needs all information to be encrypted, the entire document can be encrypted as an octet sequence.

##### To Note

-   The `<EncryptedData>` element cannot be nested, but an `<EncryptedData>` tag can be applied at the same level as another `<EncryptedData>` tag, resulting in an already encrypted data to be encrypted again.
    
-   The `EncryptionMethod` is basically a secret key mechanism such as RC4 or 3DES, RSA public key algorithm, etc depending on the level of protection required.
    
-   All the encrypted items within a document are contained in a reference list.
    
-   A URI can be employed to point to the encrypted data

##### XML Signature

**XML Signature** can be used to ensure that the document or part(s) of the document have not been tampered with maliciously before reaching the recipient

It is not the obligation of the receiving application (For example, a Web service provider) to understand what has been signed, but if it can understand the signed part of the document, the signature can be analyzed to ensure that the contents have not been altered, thus ensuring the authenticity of the document's author.

Applications may sign multiple data objects, some of which may not be XML.

An XML Signature can be applied to the content of one or more parts within an XML document.

> XML Signature has also been designed to support binary objects and multimedia types in addition to XML elements and attributes.

##### XML Signature

[Youtube](https://youtu.be/UYQPkWDaHHM)

The data objects are **canonicalized** and **digested** before being sent.

-   Digesting applies a **hash algorithm** over the data object.
-   Canonicalization removes all white space and restructures the document based on the **canonicalization algorithm**.

Before signing data, canonicalization of data is done to ensure that the same results are obtained every time.