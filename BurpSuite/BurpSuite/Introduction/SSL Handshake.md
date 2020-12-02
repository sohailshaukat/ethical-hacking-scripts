Behind HTTPs, SSL certificate plays an important role in building trust between a browser and a web server.

![[Pasted image 20201202162123.png]]

STEPS:

1. Browser requests secure pages (HTTPS) from a webserver
2. Server sends it's public key with it's SSL certificate which is digitally signed by a third party or we call Certificate Authority, or simply CA.
3. Once browser get's certificate, it will check the issuer's digital signature to make sure certificate is valid.
	1. As we know digital signature is created by CA's private key.
	2. Browsers have pre installed major CA's public key. Thus the digital signature can be verified.
	3. Once certificate's signature is verified the digital certificate can be trusted.
	4. A green padlock icon appears in address bar. Verification is done. 
4. Browser creates one symmetric key or shared secret. Keeps one and shares one with server. Before sharing secret key it uses webserver public key to encrypt the secret key and then sends it to web server.
5. When the webserver gets the encrypted symmetric key, it decrypts it using the server's private key. Now webserver has browser's shared key. From now on the traffic between webserver and browser will be encrypted and decrypted with the same key.

In this example, we actually demonstrate how asymmetric key algorithm and symmetric key algorithm work together.