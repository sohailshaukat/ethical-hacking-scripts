[[Insecure-Deserialization]]

[Youtube](https://www.youtube.com/watch?v=EzOquQNQAUs)

# Insecure Deserialization - Demonstration

## Scenario : 
- An example would be a game that stores the state locally as an object.
- When a game is finished, the state would be sent to the server that logs all the high scores.
- It is not possible to directly send the object, which is why it is serialized.
- ![[Pasted image 20201213232952.png]]
- The server now retrieves the data from the client, but to do anything with the data, the server needs to reverse the serialization process. **Deserialization**.
- ![[Pasted image 20201213233059.png]]
- Developers know to sanitize normal user input as it contain anything, but as serialized data is handled as an object, this is often forgotten.
- With the gamestate object in mind think about the following SQL-query:
	- `"SELECT score FROM highscore WHERE user = '" + gamestate.username + "';"`
	- An attacker could inject a SQL Injection payload directly into the serialized object.
	- ![[Pasted image 20201213233648.png]]
- The server would deserialize the data and then use it as the object.
	- ![[Pasted image 20201213233815.png]]
	- ![[Pasted image 20201213233838.png]]
- Insecure Deserialization is about abusing the trust developers have in objects that are often not considered as dangerous as classic user input.
- When normal URL parameters get stuck in sanitization. This can be a way in for the attacker.
- ![[Pasted image 20201213234214.png]]