#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number = len(sys.argv)
    y = 0
    for i in range(1, number):
        z = int(sys.argv[i])
        y = y + z
    print("{}".format(y))
