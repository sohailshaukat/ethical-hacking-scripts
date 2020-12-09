[[SQL-Injection]]
[Youtube](https://www.youtube.com/watch?v=1Qs195_8hNw&feature=emb_logo)

# Blind SQLinjections
-	Blind sql injections are the examples where there is no error message shown.
-	> In real life scenarios I always go through pages looking for Blind SQL injections, instead of obvious ones by using single quote. When I try to check for the existence of SQL injection, what I try is first a true statement and then a false statement and check if the page behaves any different.
		
	\- Zaid Sabih

- 
	- ` 1' and 1=1 <- True`
	- ` 1' and 1=0 <- False`
	- ` 1' order by 1 <- True`
	- ` 1' order by 100000000 <- False`


	
