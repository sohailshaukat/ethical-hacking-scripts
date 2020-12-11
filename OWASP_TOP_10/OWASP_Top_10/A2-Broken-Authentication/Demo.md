[Youtube](https://www.youtube.com/watch?time_continue=173&v=hRu_k5qt74g&feature=emb_logo)

[[BrokenAuthentication+SessionManagement]]
[[Authentication-Attacks]]
[[BrokenAuthenticationExplained]]
# Broken Authentication Demo
1. Grab sessionID for User1. Let's say PHPSessionID="XXXX1".
2. Try to intercept User2's session and replace the sessionId in requests, with User1's session ID. (In Burp).
3. Voila, do crazy shit now.

