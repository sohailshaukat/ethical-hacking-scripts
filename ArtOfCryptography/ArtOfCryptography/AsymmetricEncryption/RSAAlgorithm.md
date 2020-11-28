The RSA algorithm was developed in the year 1977 and named after its inventors Ron Rivest, Adi Shamir, and Len Adleman.

RSA is rooted in the fact that factorizing large integers is a complex task.

The public key comprises two numbers in which one is the product of two large prime numbers.

The private key is generated from the two large prime numbers. Hence the secrecy is highly dependent on the inability to factorize the large numbers.

Thus, the strength of the algorithm can be improved significantly by increasing the key size.

As of now, key sizes of 1024, 2048 or 4096 bits are used, breaking which seems to be an impossible task.


Encrypt m^e mod n = c

Decrypt c^d mod n = m

e and n form public key

d is private

[[AsymmetricEncryption]]