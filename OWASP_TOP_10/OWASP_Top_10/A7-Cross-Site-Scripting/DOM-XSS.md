[[Cross-Site-Scripting]]

![[Pasted image 20201213154329.png]]

# DOM XSS
- This occurs when the Document Object Model (DOM) environment is changed, but the code remains the same.

## Demo
[Youtube](https://www.youtube.com/watch?v=U6HXkXXx920)
- ![[Pasted image 20201213161605.png]]
- ![[Pasted image 20201213161742.png]]
- ![[Pasted image 20201213162214.png]]
- Google search 
	- `inurl:com/login?cancel_uri=`
	- `inurl:com/login?ret=`
	- `inurl:com/view.php?returnurl=`
	- `inurl:com/return.php?url=`