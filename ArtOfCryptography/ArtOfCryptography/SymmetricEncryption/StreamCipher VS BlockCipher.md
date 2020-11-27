Block Cipher

Symmetric encryption
	not used in asymmetric encrption
	
Encrypt fixed-length groups
	Often 64-bit or 128-bit blocks
	Pad added to short blocks
	
Confusion
	Key to ciphertext relationship should be very complicated
	Can't determine the key based on the ciphertext
	
Diffusion
	Output should depend on the input in a complex way
	Change one bit of the input, at least 50% of the output should be different
	

Stream Cipher

Symmetric encryption
	not used in asymmetric encrption
	
Encryption is done one byte or byte at a time
	High speed, low hardware complexity
	
The starting state should never be the same twice
	Key is often combined with an inintialization vector(IV)