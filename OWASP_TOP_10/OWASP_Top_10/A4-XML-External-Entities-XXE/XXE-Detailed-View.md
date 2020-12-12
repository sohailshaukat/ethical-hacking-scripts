[[XML-External-Entity]]
[Youtube](https://www.youtube.com/watch?v=BZOg_NgvP18)
# XXE-Detailed-View
- XML is a useful data format as data file can be checked for correctness before being processed . The structure of an XML document can be validated against document type definition **DTD** for correctness.
- **DTDs can refer to external entities.** In the process of resolving external entities an XML parser may consult various networking protocols.

		By making clever use of external entity refernces an attacker can probe your server for files.

- Example Scenario : 
	- OpenID is a popular authentication scheme implemented by web developers who want to use a third-party identity provider. **Log in with Google** is an example of OpenID.
	- With OpenID the workflow is generally performed by redirects between the site the user is seeking to log into, *the relying party* . And *the identity provider*.
	- Version 2 of openID specification allows for service discovery via XML. If openID implementation is insecure this allows harmful XML to be injected.
	- ![[Pasted image 20201212185546.png]]