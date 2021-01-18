[About](https://www.cgisecurity.com/csrf-faq.html#about)  
[**What is Cross Site Request Forgery?**](https://www.cgisecurity.com/csrf-faq.html#whatis)  
[**Who discovered CSRF?**](https://www.cgisecurity.com/csrf-faq.html#discovered)  
[**What can be done with CSRF?**](https://www.cgisecurity.com/csrf-faq.html#csrfuses)  
[**Is CSRF and Cross-site Scripting the same thing?**](https://www.cgisecurity.com/csrf-faq.html#xssvscsrf)  
[**What are common ways to perform a CSRF attack?**](https://www.cgisecurity.com/csrf-faq.html#attackperform)  
[**Is this vulnerability limited to browsers?**](https://www.cgisecurity.com/csrf-faq.html#vulnscope)  
[**Can applications using only POST be vulnerable?**](https://www.cgisecurity.com/csrf-faq.html#post)  
[**How do I detect if a website is vulnerable?**](https://www.cgisecurity.com/csrf-faq.html#detection)  
[**Can CSRF be prevented by implementing referrer checking?**](https://www.cgisecurity.com/csrf-faq.html#referer)  
[**Has a vulnerability in a major site been discovered?**](https://www.cgisecurity.com/csrf-faq.html#majorattack)  
[**What can I do to protect myself as a user?**](https://www.cgisecurity.com/csrf-faq.html#protectuser)  
[**What can I do to protect my own applications?**](https://www.cgisecurity.com/csrf-faq.html#protectapp)  
[**References and Additional Reading**](https://www.cgisecurity.com/csrf-faq.html#references)

  

### About

This paper serves as a living document for Cross-Site Request Forgery issues. This document will serve as a repository of information from existing papers, talks, and mailing list postings and will be updated as new information is discovered.

### What is Cross Site Request Forgery?

Cross Site Request Forgery (also known as [XSRF](https://www.cgisecurity.com/articles/csrf-faq.shtml), [CSRF](https://www.cgisecurity.com/articles/csrf-faq.shtml), and [Cross Site Reference Forgery](https://www.cgisecurity.com/articles/csrf-faq.shtml)) works by exploiting the trust that a site has for the user. Site tasks are usually linked to specific urls (Example: http://site/stocks?buy=100&stock=ebay) allowing specific actions to be performed when requested. If a user is logged into the site and an attacker tricks their browser into making a request to one of these task urls, then the task is performed and logged as the logged in user. Typically an attacker will embed malicious HTML or JavaScript code into an email or website to request a specific 'task url' which executes without the users knowledge, either directly or by utilizing a Cross-site Scripting Flaw. Injection via [light markup languages such](https://en.wikipedia.org/wiki/Lightweight_markup_language) as [BBCode](https://en.wikipedia.org/wiki/BBCode) is [also entirely possible](http://www.webappsec.org/lists/websecurity/archive/2007-01/msg00158.html). These sorts of attacks are fairly difficult to detect potentially leaving a user debating with the website/company as to whether or not the stocks bought the day before was initiated by the user after the price plummeted.

### Who discovered CSRF?

In the 1988 Norm Hardy published a document explaining an application level trust issue he called a [confused deputy](https://www.cis.upenn.edu/~KeyKOS/ConfusedDeputy.html). In 2000 a post to [bugtraq](http://archive.cert.uni-stuttgart.de/archive/bugtraq/2000/05/msg00141.html) explained how [ZOPE was affected](http://www.zope.org/Members/jim/ZopeSecurity/ClientSideTrojan) by a [confused-deputy](https://en.wikipedia.org/wiki/Confused_Deputy) web problem that we would define today as a [CSRF vulnerability](https://www.cgisecurity.com/articles/csrf-faq.shtml). Later in 2001 Peter Watkins posted an [entry](http://www.tux.org/~peterw/csrf.txt) on the bugtraq mailing list coining the CSRF term in response to another thread titled [The Dangers of Allowing Users to Post Images](http://archive.cert.uni-stuttgart.de/archive/bugtraq/2001/06/msg00190.html).

### What can be done with CSRF?

Most of the functionality allowed by the website can be performed by an attacker utilizing CSRF. This could include posting content to a message board, subscribing to an online newsletter, performing stock trades, using an shopping cart, or even sending an e-card. CSRF can also be used as a vector to exploit existing [Cross-site Scripting flaws](https://www.cgisecurity.com/articles/xss-faq.shtml) in a given application. For example imagine an [XSS](https://www.cgisecurity.com/articles/xss-faq.shtml) issue on an online forum or blog, where an attacker could force the user through CSRF to post a copy of the next big website worm. An attacker could also utilize CSRF to relay an attack against a site of their choosing, as well as perform a Denial Of Service attack in the right circumstances.

### Is CSRF and Cross-site Scripting the same thing?

[Cross-Site Scripting](https://www.cgisecurity.com/articles/xss-faq.shtml) exploits the trust that a client has for the website or application. Users generally trust that the content displayed in their browsers was intended to be displayed by the website being viewed. The website assumes that if an 'action request' was performed, that this is what the user wanted and happily performs it. [CSRF](https://www.cgisecurity.com/articles/csrf-faq.shtml) exploits the trust that a site has for the user.

### What are common ways to perform a CSRF attack?

The most popular ways to execute [CSRF attacks](https://www.cgisecurity.com/articles/csrf-faq.shtml) is by using a HTML image tag, or JavaScript image object. Typically an attacker will embed these into an email or website so when the user loads the page or email, they perform a web request to any URL of the attackers liking.  Below is a list of the common ways that an attacker may try sending a request.

HTML Methods

 

**IMG SRC**  
`  <img src="http://host/?command">`

 

**SCRIPT SRC**  
  `<script src="http://host/?command">`

 

**IFRAME SRC**  
  `<iframe src="http://host/?command">`

JavaScript Methods

**'Image' Object**  
```
<script>  
  var foo = new Image();  
  foo.src = "http://host/?command";  
  </script>

 ```

**'XMLHTTP' Object** (See "Can applications using only POST be vulnerable?" for when this can be used)  
  **IE** 
  ```
  <script>  
  var post\_data = 'name=value';  
  var xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");  
  xmlhttp.open("POST", 'http://url/path/file.ext', true);  
  xmlhttp.onreadystatechange = function () {  
  if (xmlhttp.readyState == 4)  
  {  
  alert(xmlhttp.responseText);  
  }  
  };  
  xmlhttp.send(post\_data);  
  </script>

 
```
**Mozilla**  
```
  <script>  
  var post\_data = 'name=value';  
  var xmlhttp=new XMLHttpRequest();  
  xmlhttp.open("POST", 'http://url/path/file.ext', true);  
  xmlhttp.onreadystatechange = function () {  
  if (xmlhttp.readyState == 4)  
  {  
  alert(xmlhttp.responseText);  
  }  
  };  
  xmlhttp.send(post\_data);  
      </script>
```
Many other ways exist in HTML/VBScript/JavaScript/ActionScript/JScript and other markup languages to make the users browser perform remote requests.

### Is this vulnerability limited to browsers?

Absolutely not. An attacker could embed scripting into a word document, Flash File, Movie, RSS or Atom web feed, or other document format allowing scripting. Applications utilizing XML documents use XML parsers to quickly parse through data. Certain tags within an XML document may tell the XML parser to request additional documents from a URI. Browsers will be the dominant way to execute these attacks but aren't the only way.

### Can applications using only POST be vulnerable?

Yes. An attacker could craft a web form on site A and using JavaScript auto submit the form to a target location of Site b. If the application containing the CSRF payload uses a browser component that runs in the local zone, then sending remote POST requests to any website is possible using XMLHTTP or similar objects.

There's another way to attack a website using purely POST based parameters, however this depends entirely on how the web application was developed. Popular web based libraries such as Perl's CGI.PM module allow a developer to fetch a parameter without caring if it came in through a GET or POST request. As is the case with certain usages of CGI.PM, POST requests can be converted to GET by the attacker and the application action will still be performed. Below is an example.

**Perl's CGI.PM**  
\------------------------------  
use CGI qw(:all);  
$value = param('foo');  
print "Content-type: text/html\\n\\n";  
print "The 'foo' parameter value is $value\\n\\n\\n";  
\------------------------------

This script allows either a GET or POST request to be sent the application. This is not limited to Perl and can affect any language depending on the library they are using, or way the application was developed. If you are using CGI.pm and want to prevent GET requests one way is to perform a request method check before executing the rest of your code using '$ENV{'REQUEST\_METHOD'}'. Below are the most common ways to fetch a parameter by language, that allow for either GET or POST requests to be sent.

**JSP Example**

 

**Commonly Used**: request.getParameter("foo")  
  **Solution**: Check the HTTP Request method and see if it is using POST before performing the requested action.

**PHP Example**

 

**Commonly Used**: $\_REQUEST\['foo'\]  
   **Solution**: Use $\_POST\['foo'\] instead to specify POST Only.

**ASP.NET Example**

 

**Commonly Used**: Request.Params\["foo"\];  
   **Solution**: Use HTTPRequest.Form (Request.Form) which grabs POST only.

Converting actions to POST only **is not a solution to CSRF**, but should be implemented as a best practice. See "What can I do to protect my own applications?" for a more comprehensive solution.

### How do I detect if a website is vulnerable?

If your website allows performing a site function using a static URL or POST request (i.e. one that doesn't change) then it is possible. If this command is performed through GET then it is a much higher risk. If the site is purely POST see "Can applications using only POST be vulnerable?" for use cases. A quick test would involve browsing the website through a proxy such as Paros and record the requests made. At a later time perform the same action and see if the requests are performed in an identical manner (your cookie will probably change). If you are able to perform the same function using the GET or POST request repeatedly then the site application may be vulnerable.  
  

### Can CSRF be prevented by implementing referrer checking?

No for two reasons.

First there are many ways that a [Referer header](https://en.wikipedia.org/wiki/HTTP_referrer) can be [blanked out](http://www.slightlyshadyseo.com/index.php/controlling-your-referer-and-hiding-your-traffic-sources/) or modified such as via web filtering software, parental control software, privacy software, proxies, or DOM trickery. This makes the referer header unreliable by nature.

Second Referer headers can be spoofed using [XMLHTTP](https://en.wikipedia.org/wiki/XMLHttpRequest) and by [using flash](http://www.securityfocus.com/archive/1/443391) as demonstrated by Amit Klein and [rapid7](http://www.rapid7.com/advisories/R7-0026.jsp). While these particular methods have been patched by the vendors, not every user visiting your website has applied these patches. Even if they did the first issue would still exist.

### Has a vulnerability in a major site been discovered?

A [vulnerability in GMail](http://www.oreillynet.com/xml/blog/2007/01/gmail_exploit_contact_list_hij.html) was discovered in January 2007 which allowed a attacker to steal a [GMail user's contact list](https://betterexplained.com/articles/gmail-contacts-flaw-overview-and-suggestions/). A different issue was discovered in [Netflix](https://jeremiahgrossman.blogspot.com/2006/10/more-on-netflixs-csrf-advisory.html) which allowed an attacker to change the name and address on the account, as well as add movies to the rental queue etc...

### What can I do to protect myself as a user?

Nothing. The fact is as long as you visit websites and don't have control of the inner architecture of these applications you can't do a thing.  The truth hurts doesn't it?   

### What can I do to protect my own applications?

The most popular suggestion to preventing CSRF involves appending non predictable challenge tokens to each request. It is important to state that this challenge token MUST be associated with the user session, otherwise an attacker may be able to fetch a valid token on their own and utilize it in an attack. In addition to being tied to the user session it is important to limit the time period to which a token is valid. This method is [documented](http://shiflett.org/articles/cross-site-request-forgeries) in multiple [documents](http://www.isecpartners.com/files/XSRF_Paper_0.pdf) however as pointed out in [mailing list postings](http://www.webappsec.org/lists/websecurity/archive/2007-01/msg00157.html) an attacker can utilize an existing browser vulnerability or [XSS flaw](https://www.cgisecurity.com/articles/xss-faq.shtml) to grab this session token.

### References and Additional Reading

\- [Wikipedia Confused Deputy Entry](https://en.wikipedia.org/wiki/Confused_Deputy)  
\- [Sending arbitrary HTTP requests with Flash 7/8 (+IE 6.0)](http://www.securityfocus.com/archive/1/443391)  
\- [HTTP Header Injection Vulnerabilities in the Flash Player Plugin](http://www.rapid7.com/advisories/R7-0026.jsp)  
\- [Client-side Trojans  (or "Browsial Engineering"?)](http://shh.thathost.com/text/client-side-trojans.txt)  
\- [Gmail Vulnerable to CSRF](http://getahead.ltd.uk/blog/joe/2007/01/01/csrf_attacks_or_how_to_avoid_exposing_your_gmail_contacts.html)  
\- [First CSRF Post to Bugtraq](http://www.tux.org/~peterw/csrf.txt)  
\- [Wikipedia XMLHTTP Entry](https://en.wikipedia.org/wiki/XMLHttpRequest)  
\- [Adobe Reader XML External Entity Attack](http://shh.thathost.com/secadv/adobexxe/)  
\- [MSDN HttpRequest.Form Property](http://msdn2.microsoft.com/en-us/library/system.web.httprequest.form.aspx)  
\- [PHP Predefined Variables List](http://www.php.net/manual/en/reserved.variables.php#reserved.variables.request)  
\- [Myspace CSRF and XSS Worm (Samy)](http://shiflett.org/archive/158)  
\- [Cross Site Reference Forgery, 2005](http://www.isecpartners.com/files/XSRF_Paper_0.pdf)  
\- [RFC 2616, "Hypertext Transfer Protocol -- HTTP/1.1"](https://www.ietf.org/rfc/rfc2616.txt)