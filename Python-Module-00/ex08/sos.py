import sys

MORSE_CODE_DICT = { ' ':'/', 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', }

def valid_arg(argv):
    for arg in argv:
        for letter in arg:
            if not letter.isalnum() and letter != ' ':
                print ("ERROR")
                sys.exit(2)

def main(argv):
    if len(argv) > 0:
        valid_arg(argv)
        i = 0
        for arg in argv:
            for letter in arg:
                print(MORSE_CODE_DICT[letter.upper()], end=' ')
            if i + 1 < len(argv):
                print(MORSE_CODE_DICT[' '], end = " ")
            i += 1
    print("")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    sys.exit(1)