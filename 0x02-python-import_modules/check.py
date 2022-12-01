#!/usr/bin/python3
array = ["John","_Peter","Sam","_Jake"]
for i in range(0, len(array)):
    if array[i].startswith("_"):
        print("{}".format(array[i][1:]))
