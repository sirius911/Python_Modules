import sys

def count_upper(string):
    total = 0
    for c in string:
        if c.isupper():
            total += 1
    return total

def count_lower(string):
    total = 0
    for c in string:
        if c.islower():
            total += 1
    return total

def count_space(string):
    total = 0
    for c in string:
        if c == ' ':
            total += 1
    return total

def count_punctuation(string):
    total = 0
    for c in string:
        if c in ".,?!;:()[]'\"-":
            total += 1
    return total

def valid(argv):
    if argv == '':
        return True
    for car in argv:
        if not car.isdigit():
            return True
    return False

def text_analyzer(argv = ''):
    """
    This function analyzes a string passed as a parameter. 
    Usage: text_analyzer(string)

    Description:
        The text analyzer() function displays the total character count,
        the number of lowercase letters, uppercase letters, spaces,
        and punctuation characters.

        NB. If more than one argument is given to the function,
            the function prints 'Error'.
            If no argument is given to the function,
            a prompt allows you to enter the character string

    Return:
        Nothing
    """
    if not valid(argv):
            print("AssertionError: argument is not a string")
            return
    string = str(argv)
    while string == '':
        string = input("What is the text to analyse?\n>> ")
    if not valid(string):
        print("AssertionError: argument is not a string")
        return
    size = len(string)
    print (f"The text contains {size} character(s):")
    print (f"- {count_upper(string)} upper letter(s)")
    print (f"- {count_lower(string)} lower letter(s)")
    print (f"- {count_punctuation(string)} punctuation mark(s)")
    print (f"- {count_space(string)} space(s)")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Error")
        sys.exit(2)
    if len(sys.argv) == 1:
        text_analyzer("")
    else:
        text_analyzer(sys.argv[1])
    sys.exit(1)