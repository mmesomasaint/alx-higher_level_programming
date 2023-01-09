#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    count = len(sys.argv)
    if count > 0:
        for i in range(count):
            result += int(sys.argv[i])
    print("{:d}".format(result))
