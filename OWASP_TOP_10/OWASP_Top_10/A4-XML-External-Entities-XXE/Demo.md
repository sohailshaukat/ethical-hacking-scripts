[[XML-External-Entity]]
[Youtube](https://www.youtube.com/watch?v=urQZZJ8iDB8)

# XXE Demonstration
- Attack agains application which parses XML data
- An attacker can abuse this parsing by reading system internal files using XML.
- System keyword is used to access particular resource on any remote server.
- If a page takes an argument/parameter in the form of XML (E.g. `https://XXXXX.com/example.php?xml=<test>lol</test>`)
	- And shows the value inside the tag on page, i.e. Hello *lol* 
	- Attacker can exploit, by using XXE payloads to view server internal files by refering to external entities.
		- E.g. `<!DOCTYPE test [<!ENTITY xxe SYSTEM "file://etc/passwd">]><test>&xxe;</test>`
		- If we're passing such payload via URL, make sure to url encode them.
		- ![[Pasted image 20201213002510.png]]
