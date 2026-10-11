#!/usr/bin/env python3
alphabet = ""
for i in range(97, 123):
    if chr(i) != 'e' and chr(i) != 'q':
        alphabet += chr(i)
print("{}".format(alphabet), end="")
