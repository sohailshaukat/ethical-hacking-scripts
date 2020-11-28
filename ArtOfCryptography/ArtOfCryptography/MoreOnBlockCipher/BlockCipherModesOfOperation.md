Block Cipher Modes of Operation

Block ciphers can be implemented using various modes of operation.

Some of the most common block cipher modes of operation are:

    Electronic Code Book
    Cipher Block Chaining
    Cipher Feedback Mode
    Output Feedback Mode
    Counter Mode

Encrypt one fixed-length group of bits at a time
	-A block
	
Mode of operation
	-Defines the method of encryption
	-May provide a method of authentication
	
The block size is a fixed size
	-Not all data matches the block size perfectly
	-Split your plaintext into smaller blocks
	-Some modes require padding before encrypting


ECB (Electronic codebook)

The simplest encryption mode
	-Too simple for most use cases
	
Each block is encrypted with the same key
	-Identical plaintext blocks create identical ciphertext blocks
	
	
![[Pasted image 20201127180440.png]]


CBC (Cipher Block Chaining)

A popular mode of operation
	-Relatively easy to implement
	
Each plaintext block is XORed with the previous ciphertext block
	-Adds additional randomization
	-Use an initialization vector for the first block
	
![[Pasted image 20201127180658.png]]


CTR (Counter)

Block cipher mode / acts like a stream cipher
	-Encrypts successive values of a counter
	
Plaintext can be any size, since it's a part of the XOR
	-i.e., 8 bits at a time (streaming) instead of a 128-bit block
	
![[Pasted image 20201127180923.png]]

GCM (Galois/Counter Mode)

Encryption with authentication
	-Authentication is part of the block mode
	-Combines counter mode with Galois authentication

Minimum latency, minimum operation overhead
	-Very efficient encryption and authentication
	
![[Pasted image 20201127181113.png]]

[[BlockCiphers]]