import sys
import re

def valid_int(val):
    try:
        return int(val)
    except ValueError:
            print("ERROR")
            sys.exit(2)

def main(argv):
    if len(argv) == 3:
        nb = valid_int(argv[2])
        words = [word for word in re.split("[ ,.;:!?]", argv[1]) if len(word) > nb]
        print (words)
    else:
        print("ERROR")
        sys.exit(2)

if __name__ == "__main__":
    main(sys.argv)
    sys.exit(1)