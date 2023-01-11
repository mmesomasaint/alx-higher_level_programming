#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    total = 0
    if len(sys.argv) > 0:
        for i in sys.argv:
            total += int(i)
    print("{:d}\n".format(total))
