#! /usr/bin/python3

import requests

response_text = requests.post("http://www.hackthissite.org/missions/realistic/10/staff.php?username=smiller&password=smiller",cookies={"HackThisSite":"ndnoqlp4ekuiv926knlkjf0jd5"})

print(response_text.text)