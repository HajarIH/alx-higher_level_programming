#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    add = 0
    
    for i in range(count):
        add = add + int(sys.argv[i + 1])
    print(add)
