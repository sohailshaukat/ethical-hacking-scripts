#! /usr/bin/python3

with open('input.txt','r') as file:
    encrypted_string = file.read().replace("\n","").split(".")

del encrypted_string[0]    


characters = []
group = []

for i, num in enumerate(iter(encrypted_string)):
    if i and not i%3:
        characters.append(sum(group))
        group = []
    group.append(int(num))

token = input("[*] Enter a token word:")

for offset in range(min(characters)-256, min(characters)+1):
    decrypted_text = "".join([chr(char-offset) for char in characters])
    if token.lower() in decrypted_text.lower():
        print("[+] Found it!")
        print(decrypted_text)
