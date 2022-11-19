import sys

def usage():
    print("USAGE: whois.py X")
    print("\t with X is an int")
    sys.exit(2)

def ft_atoi(s):
    sign, ret, i = 1, 0, 0
    s = s.strip()

    #Sign of number
    if (s[i] == '-' or s[i] == '+'):
        sign = 1 if s[i] == '+' else -1
        i += 1

    while (i < len(s)):
        if s[i] < '0' or s[i] > '9':
            raise AssertionError("argument is not integer")
        ret = 10 * ret + (ord(s[i]) - ord('0'))
        i += 1
    return sign * ret

def main(argv):
    if len(argv) == 0:
        usage()
    try:
        assert (len(argv) == 1), "more than one argument is provided"
        number = ft_atoi(argv[0])

    except AssertionError as e:
        print("AssertionError:",str(e))
        exit(2)

    if number == 0:
        print("I'm Zero.")
    elif number % 2 == 0:
        print ("I'm Even.")
    else:
        print ("I'm Odd.")
        
if __name__ == "__main__":
    main(sys.argv[1:])
    sys.exit(1)