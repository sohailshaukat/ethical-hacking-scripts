[[Insecure-Deserialization]]
# Preventing Insecure Deserialization

- Avoid serialization where it is unnecessary.
- Research and use best-practices, do not invent your own.
- Avoid allowing objects from untrusted sources.
- Use signatures to avoid tampering.
- Use encryption in-transit to protect objects.
- Use whitelisting of expected types/data.
- Use sandbox deserialization.
- Ensure logging for unexpected behavior.
- Add a question in the code review checklist.