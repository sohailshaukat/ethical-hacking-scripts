[[OWASP-Into]]

![[Pasted image 20201213232205.png]]
[Youtube](https://www.youtube.com/watch?v=nkTBwbnfesQ)

# Insecure Deserialization
- Serialization and Deserialization is the process of converting object to byte streams.
- If an attacker can manipulate input in a way that after the input is deserialized the byte stream is malicious.
- In above example attacker changes the input in such a way that super cookie of the php forum has now different user id and role. Since input is not well validated, this will result in privilege escalation post deserialization.

