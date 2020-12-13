[[XML-External-Entity]]

# Preventing XXE Attacks
- Remove the dependency on XML
- Upgrade XML parsers because later versions are more secure
- Disable entity processing on the parser
- Use timeouts to protect agains tarpit attacks
- Set memory limit
- Use whitelisting
- Use signatures to prevent tampering with uploads