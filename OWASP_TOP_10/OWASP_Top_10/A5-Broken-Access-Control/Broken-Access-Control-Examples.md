[[Broken-Access-Control]]
# Broken Access Control - Examples

## Example #1
- An attacker modifies the `User` parameter in the browser to get whatever user details they want. If not properly verified, the attacker can access any user's account.
	- http://example.com/app/userInfo?User=255

## Example #2 
- An attacker can force links to open specified URLs.
	- http://example.com/user_page
	- http://example.com/admin_page
- If an unauthenticated user can access either page, it is a flaw. If a non-admin user can access the admin page, it is a flaw.