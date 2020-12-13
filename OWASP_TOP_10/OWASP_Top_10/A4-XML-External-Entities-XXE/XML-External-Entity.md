[[OWASP-Into]]

![[Pasted image 20201212191550.png]]

[Pentester's lab](https://pentesterlab.com/exercises/play_xxe/course)

# XML External Entity
- XML External Entity (XXE) Injection is a dangerous vulnerability that allows an attacker to read local files from the server, access internal network, scan internal ports, or execute commands on remote server. It targets applications that parse XML, and occurs when the XML input contains references to an external entity, and is processed by an XML Parser that is weakly configured.
- The attacker embeds malicious XML input and expands the entities, resulting in gaining access to the web server files and remote file system, and therby establishes connections to the host over HTTP/HTTPS.

