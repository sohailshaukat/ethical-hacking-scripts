[[Injection]]
# How to prevent injection attacks?
- Always sanitize user input data.
- Keep data separate from commands and queries.
- Parameterize queries to allow the framework to escape the user input.
- Apply input validation on the server-side to all user input, however, do not rely on the input validation alone.