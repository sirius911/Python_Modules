import sys

def switchCase(c):
    if c.isalpha():
        if c.islower():
            return c.upper()
        else:
            return c.lower()
    else:
        return c


def main(argv):
    str = ''
    if len(argv) == 0:
        return
    for word in reversed(argv):
        w = reversed(list(word))
        for c in w:
            str += switchCase(c)
        str += ' '
    print(str.rstrip())
    
if __name__ == "__main__":
    main(sys.argv[1:])
    sys.exit(1)