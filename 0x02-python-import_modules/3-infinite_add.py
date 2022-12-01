#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    y = 0
    for i in sys.argv:
        i = int(i)
        y = y + i
    print("{}".format(y))
