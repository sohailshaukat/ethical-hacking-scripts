[[OWASP-Into]]

# Serialization And DeSerialziation

## Serialization: 
- Is a process of converting an object into a sequence of bytes which can be persisted to a disk or database or can be sent through streams. 

## Deserialization
- Is the reverse process of creating object from sequence of bytes.

- A Java object is a serializable if its class or any of its subclasses implements java.io.Serializable or its subinterface java.io.Externalizable interface.
- The entire process is JVM independent, meaning object can be serialized on one platform and deserialized on an entirely different platform.
- Classes ObjectInputStream and ObjectOutputStram are high-level streams can contain the methods for serializing and deserializing an object.