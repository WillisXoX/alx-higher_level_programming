#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b))) 
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b))) 
