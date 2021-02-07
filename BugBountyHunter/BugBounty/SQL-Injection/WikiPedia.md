## Technical implementations\[[edit](https://en.wikipedia.org/w/index.php?title=SQL_injection&action=edit&section=3 "Edit section: Technical implementations")\]

### Incorrectly filtered escape characters\[[edit](https://en.wikipedia.org/w/index.php?title=SQL_injection&action=edit&section=4 "Edit section: Incorrectly filtered escape characters")\]

This form of injection occurs when user input is not filtered for [escape characters](https://en.wikipedia.org/wiki/Escape_character "Escape character") and is then passed into an SQL statement. This results in the potential manipulation of the statements performed on the database by the end-user of the application.

The following line of code illustrates this vulnerability:

statement = "`SELECT * FROM users WHERE name = '`" + userName + "`';`"

This SQL code is designed to pull up the records of the specified username from its table of users. However, if the "userName" variable is crafted in a specific way by a malicious user, the SQL statement may do more than the code author intended. For example, setting the "userName" variable as:

' OR '1'='1

or using comments to even block the rest of the query (there are three types of SQL comments[\[13\]](https://en.wikipedia.org/wiki/SQL_injection#cite_note-13)). All three lines have a space at the end:

' OR '1'='1' --
' OR '1'='1' {
' OR '1'='1' /\* 

renders one of the following SQL statements by the parent language:

SELECT \* FROM users WHERE name \= '' OR '1'\='1';

SELECT \* FROM users WHERE name \= '' OR '1'\='1' \-- ';

If this code were to be used in authentication procedure then this example could be used to force the selection of every data field (\*) from _all_ users rather than from one specific user name as the coder intended, because the evaluation of '1'='1' is always true.

The following value of "userName" in the statement below would cause the deletion of the "users" table as well as the selection of all data from the "userinfo" table (in essence revealing the information of every user), using an [API](https://en.wikipedia.org/wiki/API "API") that allows multiple statements:

a';`DROP TABLE users; SELECT * FROM userinfo WHERE 't' = 't`

This input renders the final SQL statement as follows and specified:

SELECT \* FROM users WHERE name \= 'a';DROP TABLE users; SELECT \* FROM userinfo WHERE 't' \= 't';

While most SQL server implementations allow multiple statements to be executed with one call in this way, some SQL APIs such as [PHP](https://en.wikipedia.org/wiki/PHP "PHP")'s `mysql_query()` function do not allow this for security reasons. This prevents attackers from injecting entirely separate queries, but doesn't stop them from modifying queries.

### Blind SQL injection\[[edit](https://en.wikipedia.org/w/index.php?title=SQL_injection&action=edit&section=5 "Edit section: Blind SQL injection")\]

Blind SQL injection is used when a web application is vulnerable to an SQL injection but the results of the injection are not visible to the attacker. The page with the vulnerability may not be one that displays data but will display differently depending on the results of a logical statement injected into the legitimate SQL statement called for that page. This type of attack has traditionally been considered time-intensive because a new statement needed to be crafted for each bit recovered, and depending on its structure, the attack may consist of many unsuccessful requests. Recent advancements have allowed each request to recover multiple bits, with no unsuccessful requests, allowing for more consistent and efficient extraction.[\[14\]](https://en.wikipedia.org/wiki/SQL_injection#cite_note-14) There are several tools that can automate these attacks once the location of the vulnerability and the target information has been established.[\[15\]](https://en.wikipedia.org/wiki/SQL_injection#cite_note-15)

#### Conditional responses\[[edit](https://en.wikipedia.org/w/index.php?title=SQL_injection&action=edit&section=6 "Edit section: Conditional responses")\]

One type of blind SQL injection forces the database to evaluate a logical statement on an ordinary application screen. As an example, a book review website uses a [query string](https://en.wikipedia.org/wiki/Query_string "Query string") to determine which book review to display. So the [URL](https://en.wikipedia.org/wiki/URL "URL") `https://books.example.com/review?id=5` would cause the server to run the query

SELECT \* FROM bookreviews WHERE ID \= '5';

from which it would populate the review page with data from the review with [ID](https://en.wikipedia.org/wiki/Identifier "Identifier") 5, stored in the [table](https://en.wikipedia.org/wiki/Table_(database) "Table (database)") bookreviews. The query happens completely on the server; the user does not know the names of the database, table, or fields, nor does the user know the query string. The user only sees that the above URL returns a book review. A [hacker](https://en.wikipedia.org/wiki/Security_hacker "Security hacker") can load the URLs `` `https://books.example.com/review?id=5 OR 1=1` `` and `` `https://books.example.com/review?id=5 AND 1=2` ``, which may result in queries

SELECT \* FROM bookreviews WHERE ID \= '5' OR '1'\='1';
SELECT \* FROM bookreviews WHERE ID \= '5' AND '1'\='2';

respectively. If the original review loads with the "1=1" URL and a blank or error page is returned from the "1=2" URL, and the returned page has not been created to alert the user the input is invalid, or in other words, has been caught by an input test script, the site is likely vulnerable to an SQL injection attack as the query will likely have passed through successfully in both cases. The hacker may proceed with this query string designed to reveal the version number of [MySQL](https://en.wikipedia.org/wiki/MySQL "MySQL") running on the server: `` `https://books.example.com/review?id=5 AND substring(@@version, 1, INSTR(@@version, '.') - 1)=4` ``, which would show the book review on a server running MySQL 4 and a blank or error page otherwise. The hacker can continue to use code within query strings to achieve their goal directly, or to glean more information from the server in hopes of discovering another avenue of attack.[\[16\]](https://en.wikipedia.org/wiki/SQL_injection#cite_note-16)[\[17\]](https://en.wikipedia.org/wiki/SQL_injection#cite_note-17)

### Second order SQL injection\[[edit](https://en.wikipedia.org/w/index.php?title=SQL_injection&action=edit&section=7 "Edit section: Second order SQL injection")\]

Second order SQL injection occurs when submitted values contain malicious commands that are stored rather than executed immediately. In some cases, the application may correctly encode an SQL statement and store it as valid SQL. Then, another part of that application without controls to protect against SQL injection might execute that stored SQL statement. This attack requires more knowledge of how submitted values are later used. Automated web application security scanners would not easily detect this type of SQL injection and may need to be manually instructed where to check for evidence that it is being attempted.

## Mitigation\[[edit](https://en.wikipedia.org/w/index.php?title=SQL_injection&action=edit&section=8 "Edit section: Mitigation")\]

An SQL injection is a well known attack and easily prevented by simple measures. After an apparent SQL injection attack on [TalkTalk](https://en.wikipedia.org/wiki/TalkTalk_Group "TalkTalk Group") in 2015, the BBC reported that security experts were stunned that such a large company would be vulnerable to it.[\[18\]](https://en.wikipedia.org/wiki/SQL_injection#cite_note-18)

### Detection\[[edit](https://en.wikipedia.org/w/index.php?title=SQL_injection&action=edit&section=9 "Edit section: Detection")\]

SQL injection filtering works in similar way to emails spam filters. Database firewalls detect SQL injections based on the number of invalid queries from host, the presence of OR and UNION blocks inside of the request, or other characteristics.[\[19\]](https://en.wikipedia.org/wiki/SQL_injection#cite_note-19)

### Parameterized statements\[[edit](https://en.wikipedia.org/w/index.php?title=SQL_injection&action=edit&section=10 "Edit section: Parameterized statements")\]

Main article: [Prepared statement](https://en.wikipedia.org/wiki/Prepared_statement "Prepared statement")

With most development platforms, parameterized statements that work with parameters can be used (sometimes called placeholders or [bind variables](https://en.wikipedia.org/wiki/Bind_variable "Bind variable")) instead of embedding user input in the statement. A placeholder can only store a value of the given type and not an arbitrary SQL fragment. Hence the SQL injection would simply be treated as a strange (and probably invalid) parameter value. In many cases, the SQL statement is fixed, and each parameter is a [scalar](https://en.wikipedia.org/wiki/Scalar_(computing) "Scalar (computing)"), not a [table](https://en.wikipedia.org/wiki/Table_(database) "Table (database)"). The user input is then assigned (bound) to a parameter.[\[20\]](https://en.wikipedia.org/wiki/SQL_injection#cite_note-20)

Easily put, using parameterized queries can definitely prevent SQL injection. This mainly means that your variables aren't query strings that would accept arbitrary SQL inputs, however, some parameters of given types are definitely necessary. Parameterized queries require the developer to define all the code. Therefore, without parameterized queries, anyone could put any kind of SQL code into the field, and have the database erased. But if the parameters were to set to '@username' then the person would only be able to put in a username without any kind of code.[\[21\]](https://en.wikipedia.org/wiki/SQL_injection#cite_note-21)

#### Enforcement at the coding level\[[edit](https://en.wikipedia.org/w/index.php?title=SQL_injection&action=edit&section=11 "Edit section: Enforcement at the coding level")\]

Using [object-relational mapping](https://en.wikipedia.org/wiki/Object-relational_mapping "Object-relational mapping") libraries avoids the need to write SQL code. The ORM library in effect will generate parameterized SQL statements from object-oriented code.

### Escaping\[[edit](https://en.wikipedia.org/w/index.php?title=SQL_injection&action=edit&section=12 "Edit section: Escaping")\]

A straightforward, though error-prone way to prevent injections is to escape characters that have a special meaning in SQL. The manual for an SQL DBMS explains which characters have a special meaning, which allows creating a comprehensive [blacklist](https://en.wikipedia.org/wiki/Blacklist_(computing) "Blacklist (computing)") of characters that need translation. For instance, every occurrence of a single quote (`'`) in a parameter must be replaced by two single quotes (`''`) to form a valid SQL string literal. For example, in [PHP](https://en.wikipedia.org/wiki/PHP "PHP") it is usual to escape parameters using the function `mysqli_real_escape_string();` before sending the SQL query:

$mysqli \= new mysqli('hostname', 'db\_username', 'db\_password', 'db\_name');
$query \= sprintf("SELECT \* FROM \`Users\` WHERE UserName='%s' AND Password='%s'",
                  $mysqli\->real\_escape\_string($username),
                  $mysqli\->real\_escape\_string($password));
$mysqli\->query($query);

This function prepends backslashes to the following characters: `\x00`, `\n`, `\r`, `\`, `'`, `"` and `\x1a`. This function is normally used to make data safe before sending a query to [MySQL](https://en.wikipedia.org/wiki/MySQL "MySQL").[\[22\]](https://en.wikipedia.org/wiki/SQL_injection#cite_note-22)  
PHP has similar functions for other database systems such as pg\_escape\_string() for [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL "PostgreSQL"). The function `addslashes(string $str)` works for escaping characters, and is used especially for querying on databases that do not have escaping functions in PHP. It returns a string with backslashes before characters that need to be escaped in database queries, etc. These characters are single quote ('), double quote ("), backslash (\\) and NUL (the NULL byte).[\[23\]](https://en.wikipedia.org/wiki/SQL_injection#cite_note-23)  
Routinely passing escaped strings to SQL is error prone because it is easy to forget to escape a given string. Creating a transparent layer to secure the input can reduce this error-proneness, if not entirely eliminate it.[\[24\]](https://en.wikipedia.org/wiki/SQL_injection#cite_note-24)

### Pattern check\[[edit](https://en.wikipedia.org/w/index.php?title=SQL_injection&action=edit&section=13 "Edit section: Pattern check")\]

Integer, float or boolean, string parameters can be checked if their value is valid representation for the given type. Strings that must follow some strict pattern (date, UUID, alphanumeric only, etc.) can be checked if they match this pattern.

### Database permissions\[[edit](https://en.wikipedia.org/w/index.php?title=SQL_injection&action=edit&section=14 "Edit section: Database permissions")\]

Limiting the permissions on the database login used by the web application to only what is needed may help reduce the effectiveness of any SQL injection attacks that exploit any bugs in the web application.

For example, on [Microsoft SQL Server](https://en.wikipedia.org/wiki/Microsoft_SQL_Server "Microsoft SQL Server"), a database logon could be restricted from selecting on some of the system tables which would limit exploits that try to insert JavaScript into all the text columns in the database.

deny select on sys.sysobjects to webdatabaselogon;
deny select on sys.objects to webdatabaselogon;
deny select on sys.tables to webdatabaselogon;
deny select on sys.views to webdatabaselogon;
deny select on sys.packages to webdatabaselogon;