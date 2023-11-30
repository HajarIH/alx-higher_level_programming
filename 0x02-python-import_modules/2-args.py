#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    i = len(argv)
    if i == 0:
        print("0 arguments.")
    elif i == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(i))
    for j in range(i):
        print("{:d}: {:s}".format(j + 1, argv[j + 1]
