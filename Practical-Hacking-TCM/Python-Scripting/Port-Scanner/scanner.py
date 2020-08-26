#!/bin/python3

import sys
import socket
from datetime import datetime  as dt

try:

	if len(sys.argv) == 2:
		target = socket.gethostbyname(sys.argv[1])   #Translating host name to IPv4
	else:
		print("[+]Invalid amount of arguments.")
		print("[+]Syntax: python3 scanner.y <ip>")		 

	#BANNER
	print("-"*50)
	print("[+]Scanning target "+target)
	print("[+]Time started: "+ str(dt.now()))
	print("-"*50)


	for port in range(1,65534):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		results = s.connect_ex((target,port)) #returns an error indicator
		if not results:
			print("Port {} is open".format(port))
		s.close()

except KeyboardInterrupt:
	print("[-]Exiting program...")
	sys.exit()
	
except socket.gaierror:
	print("[-]Hostname could not be resolved.")
	sys.exit()
	
except socket.error:
	print("[-]Could not connect to server.")
	sys.exit()
	
