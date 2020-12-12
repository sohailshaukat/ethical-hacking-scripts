[[Sensitive-Data-Exposure]]

# How Sensitive Data Exposure Happens?
- **Hackers generally do not break into cryptography.** They often steal something which will help them break the encryption. For example, they steal keys, or clear text data from the server or from data that is encrypted and hashed with a weak algorithm.
- **Most attackers will try the following:**
	1. Decrypt data stored on a server (previously stolen through other kinds of vulnerabilities) .
	2. Intercept data between a server and the browser.
	3. Trick your web application to do things like changing the content of a cart in an e-commerce appliation, or elevating their privileges.