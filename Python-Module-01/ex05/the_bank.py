
import time


class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):

        self.__dict__.update(kwargs)

        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, "value"):
            self.value = 0

        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount


class Bank(object):
    """The bank"""
    red = "\033[91m"
    green = "\033[92m"
    yellow = "\033[93m"
    reset = "\033[0m"

    def __init__(self):
        self.accounts = []

    def is_client(self, account):
        """return True if the Account is a client otherwise False"""
        if not isinstance(account, Account):
            account = self.get_account_by_name(account)
            if account is None:
                return False
        for client in self.accounts:
            if client.name == account.name:
                return True
        return False

    def add(self, new_account):
        """ Add new_account in the Bank
            @new_account: Account() new account to append
            @return
            True if success, False if an error occured
        """
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts

        # the right object
        if not isinstance(new_account, Account):
            return False

        if self.is_client(new_account):
            # the name of the new account already exist in Bank
            print(f"'{Bank.yellow}{new_account.name}{Bank.reset}' already exist in Bank --> {Bank.red}Rejected{Bank.reset}")
            return False
        self.accounts.append(new_account)
        print(f"'{Bank.yellow}{new_account.name}{Bank.reset}' has been {Bank.green}added{Bank.reset} to our customers.")
        return True

    def transfer(self, origin, dest, amount):
        """" Perform the fund transferq
            @origin: str(name) of the first account
            @dest: str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if success, False if an error occured
        """
        result = True
        print(f"\n***************** T R A N S F E R *****************")
        print(f"*  From : {Bank.yellow}'{origin}{Bank.reset}'")
        print(f"*  to   : {Bank.yellow}'{dest}{Bank.reset}'")
        origin_account = self.get_account_by_name(origin)
        dest_account = self.get_account_by_name(dest)
        print(f"Account origin ({origin}) ", end="")
        if origin_account:
            if self.check(origin_account):
                print(f"{Bank.green}OK{Bank.reset}")
            else:
                print(f"-> {Bank.red}Corrupted{Bank.reset}")
                result = False
        else:
            print(f"{Bank.red}NOT FOUND{Bank.reset}")
            result = False
        print(f"Destination Account ({dest}) ", end="")
        if dest_account:
            if self.check(dest_account):
                print(f"{Bank.green}OK{Bank.reset}")
            else:
                print(f"-> {Bank.red}Corrupted{Bank.reset}")
                result = False
        else:
            print(f"{Bank.red}NOT FOUND{Bank.reset}")
            result = False
        if result and amount < 0:
            print(f"{Bank.red}Fail{Bank.reset} The amount must be >= 0")
            result = False
        if result and origin_account.value - amount < 0:
            print(f"{Bank.red}Fail{Bank.reset} The amount ({Bank.yellow}${amount:.2f}{Bank.reset}) is larger than the balance of the account of origin ({Bank.yellow}${origin_account.value}{Bank.reset}")
            result = False
        if result and origin_account.name != dest_account.name:
            origin_account.transfer(-amount)
            dest_account.transfer(amount)
        if result:
            print(f"\n----------------- Tranfer {Bank.green}Made{Bank.reset} -----------------")
            print(f"\tNew Value after transfert:")
            print(f"\tOrigin Account : {Bank.yellow}${origin_account.value:.2f}{Bank.reset}")
            print(f"\tDestination Account : {Bank.yellow}${dest_account.value:.2f}{Bank.reset}")
            print(f"************* {Bank.green}E N D   T R A N S F E R {Bank.reset}************")
        else:
            print(f"***** {Bank.red}T R A N S F E R    I N T E R R U P T E D{Bank.reset}*****")
        return result

    def fix_account(self, name):
        """ fix account associated to name if corrupted
            @name:str(name) of the account
            @return True if success, False if an error occured
        """
        if  isinstance(name, Account):
            if self.is_client(name):
                account_to_check = name
            else:
                account_to_check = None
        else:
            account_to_check = self.get_account_by_name(name)
            if account_to_check is not None:
                name = account_to_check.name
        print(f"********  fix account ({Bank.yellow}{name}{Bank.reset})  ********", end="")
        
        if not account_to_check:
            print(f" {Bank.red}not found{Bank.reset}")
            return False
        print("")
        # attribut starting with b
        attribut_account = dir(account_to_check)
        for a in attribut_account:
            if a[0] == 'b':
                print(f"\tattribut ({Bank.yellow}{a}{Bank.reset}) starting with 'b' ...", end="")
                delattr(account_to_check, a)
                print(f"{Bank.green}destroyed{Bank.reset}")

        # missing attribut
        missing_attribut = self.get_missing_attribut(account_to_check)
        if len(missing_attribut) > 0:
            print(f"\tmissing attribut : {Bank.red}{missing_attribut}{Bank.reset}")
            print(f"\t\t-> creation of :", end="")
            for a in missing_attribut:
                if a[-1] == '*':
                    setattr(account_to_check, a[:-1], "")
                    print(f" [{Bank.green}{a[:-1]}{Bank.reset}] ", end="")
                else:
                    setattr(account_to_check, a, "")
                    print(f" [{Bank.green}{a}{Bank.reset}] ", end="")
            print("")

        # even number of attributes
        nb_attributes = len(vars(account_to_check))
        if nb_attributes % 2 == 0:
            print(f"the number ({Bank.yellow}{nb_attributes}{Bank.reset}) of attributes is {Bank.red}Even{Bank.reset} ")
            label = "checking." + str(time.time())
            print(f"\t-> add [{Bank.green}{label}{Bank.reset}]  for new attribute.")
            setattr(account_to_check, label, "fixed")

        if self.check(account_to_check, False):
            print(f"********** {Bank.green}F I X E D{Bank.reset} *******")
            return True
        else:
            print(f"***** {Bank.red}F A I L E D{Bank.reset} ******")
            return False

    def get_account_by_name(self, name):
        """ returns Account with name or None if not found or Error"""
        try:
            for account in self.accounts:
                if account.name == name:
                    return account
            return None
        except Exception:
            return None

    def get_missing_attribut(self, account):
        """returns a list of missing attributs"""
        attribut = []
        mandatory_attributes = ["zip*", "addr*", "name", "id", "value"]
        attribut_account = dir(account)
        for a in mandatory_attributes:
            if a[-1] == '*':
                for b in attribut_account:
                    if b.find(a[:-1]) != -1:
                        attribut.append(a)
            else:
                if a in attribut_account:
                    attribut.append(a)
        setAttribut = set(attribut)
        setMandatory = set(mandatory_attributes)
        return list(setMandatory - setAttribut)

    def check(self, account, verbose=False):
        """Checking the account"""
        # Checking
        result = True

        if isinstance(account, str):
            account = self.get_account_by_name(account)
        if account is None:
            if verbose:
                print("Not Found")
                result = False

        if verbose:
            print(f"*** Checking ({account.name})")

        attributsDict = vars(account)
        # checking attribute
        if verbose:
            print("\t- Checking Attributes:")

        # mandatory Attributes
        if len(self.get_missing_attribut(account)) > 0:
            if verbose:
                print(f"\t\t- Missing attribute {Bank.yellow}{self.get_missing_attribut(account)}{Bank.reset} --> {Bank.red}reject{Bank.reset}")
            result = False
        else:
            if verbose:
                print(f"\t\t{Bank.green}All mandatory attributes is presents.{Bank.reset}")

        for key, value in attributsDict.items():
            if verbose:
                print(f"\t\t\tAttribute [{Bank.yellow}{key}{Bank.reset}] ", end="")
            if key[0] == 'b':
                # an attributes starting with 'b'
                if verbose:
                    print(f"starting with a 'b' [FORBIDDEN] -> {Bank.red}Error{Bank.reset}")
                    result = False
            elif key == "name":
                if not isinstance(value, str):
                    # name not being a string
                    if verbose:
                        print((f"not a string -> {Bank.red}reject{Bank.reset}"))
                    result = False
                else:
                    if verbose:
                        print(f"= {Bank.yellow}{type(value)}{Bank.reset} -> {Bank.green}OK{Bank.reset}")
            elif key == "id":
                if not isinstance(value, int):
                    # id not being an int
                    if verbose:
                        print(f"not an int -> {Bank.red}reject{Bank.reset}")
                    result = False
                else:
                    if verbose:
                        print(f"= {Bank.yellow}{type(value)}{Bank.reset} -> {Bank.green}OK{Bank.reset}")
            elif key == "value":
                if not isinstance(value, int) and not isinstance(value, float):
                    # value not being an int or a float
                    if verbose:
                        print(f"not an int or a float -> {Bank.red}reject{Bank.reset}")
                    result = False
                else:
                    if verbose:
                        print(f"= {Bank.yellow}{type(value)}{Bank.reset} -> {Bank.green}OK{Bank.reset}")
            else:
                if verbose:
                    print(f"{Bank.green}OK{Bank.reset}")

        # Nb of attributes
        if verbose:
            print(f"\t- Nb of attributes = {Bank.yellow}{len(attributsDict)}{Bank.reset}: ", end="")
        if len(attributsDict) % 2 == 0:
            # even numbers of attributes
            if verbose:
                print(f"{Bank.yellow}Even{Bank.reset} => {Bank.red}reject{Bank.reset}")
            result = False
        if verbose:
            print(f"{Bank.green}OK{Bank.reset}")
        if verbose:
            if result:
                print(f"*** Conclusion ------> {Bank.green}OK (not corrupted){Bank.reset}")
            else:
                print(f"*** Conclusion ------> {Bank.red}KO (corrupted){Bank.reset}")
        return result
