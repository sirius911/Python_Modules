import itertools
import random
from the_bank import Account, Bank

if __name__ == "__main__":
    bank = Bank()
    list_account = []
    list_account.append(Account('Sherlock Holmes',
                          zip='NW1 6XE',
                          addr='221B Baker street',
                          value=1000.0))
    list_account.append(Account('James Watson',
                          zip='NW1 6XE',
                          addr='221B Baker street',
                          value=25000.0,
                          info=None))
    
    list_account.append(Account("Douglass",
                            addr='boulevard bessieres',
                            value=42))
    list_account.append(Account("Adam"))

    list_account.append(Account("Bender Bending Rodríguez",
                            zip_one='1',
                            addr='Mexico',
                            value=42,
                            bzip='-42'))
                            
    bad_account1 = Account("Charlotte",
                            zip='2',
                            addr='Somewhere in the Milky Way',
                            value=42)
    list_account.append(bad_account1)
    bad_account1.value = "-42"

    list_account.append(Account("Charlotte",
                            zip='3',
                            addr='Somewhere in the Milky Way bis',
                            value=42))

    bad_account2 = Account("Edouard",
                            zip='3',
                            addr='France',
                            value=42)
    list_account.append(bad_account2)
    virus = range(1,10)
    bad_account2.id = virus
    bad_account2.name = 42
    
    print("*************************************Adding many Account...")
    for account in list_account:
        bank.add(account)
    input("Press ENTER to continue:")

    print("\n************************************************Checking")
    for account in bank.accounts:
        bank.check(account, True)
    input("Press ENTER to continue:")

    print("\n************************************************Fixing")
    for account in bank.accounts:
        if not bank.check(account):
            bank.fix_account(account.name)
    input("Press ENTER to continue:")

    print("\n************************************************Transfer")
    pair_transfer = list(itertools.permutations(bank.accounts, 2))
    for accounts in pair_transfer:
        origin = accounts[0]
        dest = accounts[1]
        try:
            if origin.value > 0:
                amount = random.randint(1, int(origin.value) * 100) / 100
            else:
                amount = random.randint(1, 10000) / 100
        except:
                amount = random.randint(1, 10000) / 100
        print(f"Transfer {Bank.yellow}${amount}{Bank.reset} from [{origin.name}]  --->  [{dest.name}]")
        bank.transfer(origin.name, dest.name, amount)