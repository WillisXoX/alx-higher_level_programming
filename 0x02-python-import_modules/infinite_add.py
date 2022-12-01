#!/usr/bin/python3
from sys import argv
userin = argv[1:]
size = len(userin)
result = 0
for i in range(0, size):
    result = result + int(userin[i])
print("sum = {}".format(result)) 
