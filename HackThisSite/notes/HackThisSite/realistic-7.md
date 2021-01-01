i noticed that images were fed to the page from a .txt file, this .txt file contained the address of images

so instead i navigated to the /images folder found in these .txt files

this folder showed me an admin directory, this directory was protected

However the showimages.php?file took arguments without any validation

so i can technically try to point it to htpassword file under admin directory and then can view the password as image's src

```
administrator:$1$AAODv...$gXPqGkIO3Cu6dnclE/sok1

(base) ┌──(baba㉿baba)-\[~/GitHub/ethical-hacking-scripts/HackThisSite/realistic\_7\]  
└─$ john htpasswd \-show   
administrator:shadow  
  
1 password hash cracked, 0 left

```

![[Pasted image 20201227210345.png]]

https://www.hostinger.in/tutorials/locate-and-create-htaccess