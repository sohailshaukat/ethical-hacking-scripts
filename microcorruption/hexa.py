#!python3
print(list(map(lambda x : hex(ord(x)), input() )))

print(list(map(lambda x : chr(int(x, 16)) , input().split(" "))))