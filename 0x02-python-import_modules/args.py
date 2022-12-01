#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    userin = argv[1:]
    size = len(userin)
    for i in range(0, size):
        print("{}".format(userin[i]))
