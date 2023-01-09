#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    result = 0
    count = len(sys.argv)
    if count == 1: 
        result = sys.argv[i]
    
    elif count > 1:
        for i in range(1, count-1):
            result += int(sys.argv[i])
    print("{:d}".format(result))
