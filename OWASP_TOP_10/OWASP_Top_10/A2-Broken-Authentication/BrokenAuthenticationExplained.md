[[Authentication-Attacks]]
[[BrokenAuthentication+SessionManagement]]
 [[A2-Broken-Authentication/Prevention]]
[Youtube](https://www.youtube.com/watch?v=mruO75ONWy8)

# BrokenAuthentication Explained
- When a user tries to log in to a web application, if the login attempt is successful user is allowed to login and a session ID is created and provided to the user's session.
- Credential Stuffing, Automated Attacks (Brute-Forcing), Default Passwords, Scenario-1
	- Scenario-1 : When a user is in public accessing webapplication, closes the tab but not the browser and leaves the machine unmonitored. A bad actor will slip in reopen a session new tab and due to the session id being saved by the browser he'll be able to access user's session.
## Prevention
-	Multi-Factor Authentication
- Password checking
	- Proactively checking if there are weak passwords in database and prompting users to change it to strong password
- Password Complexity
- Limit failed logins
- Server Side Session Management
	- Server Side SessionID  manager throws away the old client side session ID and randomly allocates a session ID server side to the current active session. Now if another user and uses old session id, he won't be able to as new one was created back side.