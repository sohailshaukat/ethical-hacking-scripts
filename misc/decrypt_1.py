#! /usr/bin/python3

import sys


def decrypt(string):
	result = []
	for pos, char in enumerate(string):
		result.append(chr(ord(char)-pos))
	return "".join(result)


print(decrypt(sys.argv[1]))
