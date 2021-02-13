#! /usr/bin/python3
import requests
import argparse
import os
import sys


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cookies", dest="cookies",
                        help="Cookies: -c PHPSESSID:f8ucrbu0qmta4ettc3208gcvnq& security:low")
    parser.add_argument("-u", "--url", dest="url", help="URL: -u http://127.0.0.1/")
    parser.add_argument("-param", "--param", dest="param",
                        help="Param: -p ID:")
    parser.add_argument("-C", "--csrfxpath", dest="csrfxpath", help="CSRF-Xpath: //input[@name='user_token']/@value")
    parser.add_argument("-PT", "--passedText", dest="passedText", help="True resulting query text: User ID exists in the database.")
    parser.add_argument("-m", "--method", dest="method", help="Method: -m get OR -m POST")
    options = parser.parse_args()
    return options


def deserializer(serialized):
    deserialized = {}
    pairs = serialized.split(";")
    if pairs[-1] == "":
        del pairs[-1]
    for pair in pairs:
        pair = pair.split(":")
        deserialized[pair[0]] = pair[1]
    return deserialized


def send_request(url, params, req_username="", req_password="", req_cookies=None, req_csrf=""):
    """
    This sends the request
    :param url: URL of the application / page
    :param params: parameters to be sent along with request. Serialized String.
    :param req_cookies: cookies to be sent along with request. DeSerialized Dictionary
    :param method: GET or POST method
    :return:
    """
    if req_cookies is None:
        req_cookies = {}
    params = deserializer(params) if params else {}
    print(f"[*]URL : {url}")
    print("[*]Cookies", req_cookies)
    print("[*]Params", params)
    if METHOD.lower() == "get":
        return requests.get(url, cookies=req_cookies, params=params)
    else:
        return requests.post(url, cookies=req_cookies, data=params)        


arguments = get_arguments()     

if arguments.method and arguments.method.lower() in ("get","post"):
    METHOD = arguments.method
elif arguments.method:
    print("[-] Please enter valid method. GET or POST.")    
    sys.exit()
else:
    METHOD = "get"


if arguments.url:
    URL = arguments.url
else:
    print("[-] Please provide either URL")
    sys.exit()    

if arguments.param:
    param = arguments.param
else:
    print("[-] Please provide injectable parameter")
    sys.exit()    

cookies = deserializer(arguments.cookies) if arguments.cookies else {}

if not arguments.passedText:
    print("[-] Please provide true resulting query / successful execution text ")
    sys.exit()

FOUND = False

CURRENT = ""

while not FOUND:
    try:
        #TODO
        
