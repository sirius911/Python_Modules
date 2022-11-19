import sys

def usage():
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("\tpython operations.py 10 3")

def ft_atoi(s):
    sign, ret, i = 1, 0, 0
    s = s.strip()

    #Sign of number
    if (s[i] == '-' or s[i] == '+'):
        sign = 1 if s[i] == '+' else -1
        i += 1

    while (i < len(s)):
        if s[i] < '0' or s[i] > '9':
            raise AssertionError("only integers")
        ret = 10 * ret + (ord(s[i]) - ord('0'))
        i += 1
    return sign * ret

def ft_division(number1, number2):
    try:
        result = number1 / number2
        return result
    except ZeroDivisionError as e:
        return "ERROR (div by zero)"

def ft_modulo(number1, number2):
    try:
        result = number1 % number2
        return result
    except ZeroDivisionError as e:
        return "ERROR (modulo by zero)"

def operation(argv):
    if(len(argv) < 3):
        usage()
        exit(2)
    try:
        assert (len(argv) == 3), "too many arguments"
        number1 = ft_atoi(argv[1])
        number2 = ft_atoi(argv[2])
        
    except AssertionError as e:
        print("AssertionError:",str(e))
        exit(2)

    #operations
    print(f"{'Sum:':<12}{number1 + number2}")
    print(f"{'Difference:':<12}{number1 - number2}")
    print(f"{'Product:':<12}{number1 * number2}")
    print(f"{'Quotient:':<12}{ft_division(number1, number2)}")
    print(f"{'Remainder:':<12}{ft_modulo(number1, number2)}")

if __name__ == "__main__":
    operation(sys.argv)
    sys.exit(1)