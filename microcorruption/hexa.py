#!python3
print("".join(map(lambda x : hex(ord(x)).replace("0x",""), input() )))

# print(list(map(lambda x : chr(int(x, 16)) , input().split(" "))))

# -8fBVvp