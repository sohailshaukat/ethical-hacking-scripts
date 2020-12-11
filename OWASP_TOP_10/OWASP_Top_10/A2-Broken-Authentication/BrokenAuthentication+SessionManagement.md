[[Authentication-Attacks]]
# Broken Authentication and Session Management

The following vulnerabilities allow an attacker to bypass the authentication methods in a web application:
- Improper authentication
- Use of single-factor authentication
- Unprotected storage of credentials
- Predictable login credentials (E.g. admin/admin)
- Exposing session IDs in the URL (E.g. URL rewriting)
- A session does not timeout (or) is not invalidated after logout
- Insufficient session expiration
- Unverified password change
- Sending passwords, session IDs, and other credentials over unencrypted connections