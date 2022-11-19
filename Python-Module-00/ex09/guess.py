from random import randint

class bcolor:
    C_GREEN = "\033[92m"
    C_RED = "\033[91m"
    C_YELLOW = "\033[93m"
    C_CYAN = "\033[94m"
    C_RESET = "\033[0m"

def main_loop(nb):
    nb_try = 0
    while 42:
        print("What's your guess between 1 and 99?")
        choice = input(">> ")
        nb_try += 1
        if choice == "exit":
            print("Goodbye!")
            break
        try:
            guess = int(choice)
            if guess == nb:
                if nb == 42:
                    print(f"The answer to the ultimate question of life, the universe and everything is {bcolor.C_GREEN}42{bcolor.C_RESET}.")
                if nb_try == 1:
                    print(f"Congratulations, you got it on your{bcolor.C_CYAN} first try{bcolor.C_RESET}!")
                else:
                    print("Congratulations, you've got it!")
                    print(f"You won in {bcolor.C_GREEN}{nb_try}{bcolor.C_RESET} attempts!")
                break
            if guess > nb:
                print(f"{bcolor.C_CYAN}Too hight!{bcolor.C_RESET}")
            else:
                print(f"{bcolor.C_YELLOW}Too low!{bcolor.C_RESET}")

        except ValueError:
            print(f"{bcolor.C_RED}That's not a number.{bcolor.C_RESET}")
            
       
def main():
    nb = randint(1, 99)
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!\n")
    main_loop(nb)

if __name__ == "__main__":
    main()