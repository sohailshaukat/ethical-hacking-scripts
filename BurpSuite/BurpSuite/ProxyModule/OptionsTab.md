This Option Tab helps to configure the Burp proxy as a browser proxy so that Burp Suite can interact with the browser proxy.

- Proxy listener

		Burp Suite Proxy accepts requests from the browser. By default, Burp listener is on port 8080. If some other application is running on port 8080, you can change the port numbers in both browser and burp suite.

- Browser proxy config

		You need to configure the browser to use the Burp Proxy listener as its proxy server for both HTTP and HTTPS protocols.

		You may refer to Install CA Certificates in Browsers from the previous section
		
- Burp CA certificate 
	
		You will get warning messages if you access a HTTPS website. It is because the browser does not recognize the SSL certificate. Hence, it shows the warning message.

		To overcome this, you need to install Burp's Certificate Authority Master certificate in your browser. So, the trust happens, and you can visit the HTTPS pages effectively.

