Turns variable-length input into a fixed-sized digest - think of a fingerprint for any given input

A good cryptographic hash function needs to be:
	Collision resistant
		It should be not feasible to find any different x,y such that H(x) = H(y)
	Infeasible to change message without changing the hash
		Any change to x creating x' should lead to a vastly different H(x')
	One-way (pre-image resistant)
		Given z, it's not feasible to find any x such that H(x) = z.
	Hash functions can be used for integrity
		If Alice sends a message and securely transmits its hash. Bob can calculate and verify the hash from the received message


Limitations
![[Pasted image 20201201152534.png]]


Hashing Functions
	DONOT USE RED ONES
	
	![[Pasted image 20201201152632.png]]
	
SHA-3 Hashing

![[Pasted image 20201201152713.png]]


Hashing

![[Pasted image 20201201153654.png]]