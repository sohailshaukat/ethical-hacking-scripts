So you’ve found a page that’s vulnerable to Local File Inclusion:  
  
![LFI-1](https://www.corben.io/images/lfi/lfi-1.png "LFI-1")  
You do some testing to leverage this vulnerability to RCE, but nothing’s working Null bytes don’t work, `/proc/self/environ` doesn’t work, and wrappers that lead to RCE such as `data://` or `php://input` do not work either. Don’t give up yet, there may be another way!  
  
Let’s start off by trying to read the source code of this page! Let’s see if `php://filter` works: `http://127.0.0.1/vuln.php?page=php://filter/convert.base64-encode/resource=vuln`  
  
![LFI-2](https://www.corben.io/images/lfi/lfi-2.png "LFI-2")  
  
Voila! It works. Once base64 decoded the code is:  
  
![LFI-3](https://www.corben.io/images/lfi/lfi-3.png "LFI-3")  
  
Now you can see how the page is being requested. It’s using include to request the page & appending the .php (ignore the commented line below it, I was was merely playing with RFI).  
  
So now we know we can read files on the site. Use this to try to find the full path of the site, since you can use it. Now say this site has a function where you can upload a profile picture or upload a picture to a gallery. Awesome, then you’re in luck!  
  
Write some php code (Ex: `<?php phpinfo(); ?>` and **compress it** to a zip file. Rename the zip file to _avatar.jpg_ (change the extension to an image file) and upload it.  
  
  
My picture is uploaded to http://127.0.0.1/avatars/myavi.jpg Now here’s the trick using the **zip://** wrapper!  
  
`zip:///path/to/filename#dir/file` (URL Encode the # to %23) when exploiting.  
  

### Example:

With full path:  
  
`http://127.0.0.1/vuln.php?page=zip:///Library/WebServer/Documents/avatars/myavi.jpg%23shell`  
  
Without full path:  
  
`http://127.0.0.1/vuln.php?page=zip://avatars/myavi.jpg%23shell`  
  
I did not have to add the .php to the end because the script will automatically appends it! Now, we have successfully leveraged this LFI to an RCE using the **zip://** wrapper!  
  
![LFI-4](https://www.corben.io/images/lfi/lfi-4.png "LFI-4")