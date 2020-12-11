[[BrokenAuthentication+SessionManagement]]
[[Authentication-Attacks]]
[[BrokenAuthenticationExplained]]

# Preventing Broken Authentication

To prevent broken authentication,
- Implement multi-factor authentication (credential stuffing, brute-force, and stolen credential re-use attacks).
- Implement weak-password checks, such as (admin/admin, user/password, and so on).
- Set complexity, password length, and rotation policies.
- Limit failed attempts and increase the delay for all failed login attempts. Log all failures, and alert administrators. This helps when credential stuffing, brute-force, or other attacks are detected.
- Use a server-side secure built-in session manager which helps generate a new random session ID after login. Ensure that session IDs are not displayed in the URL, are securely stored, and are invalidated after logout, idle, and absolute timeouts.
