from csvreader import CsvReader

if __name__ == "__main__":
    with CsvReader('good.csv',',', True, 5, 10) as file:
        if file:
            data = file.getdata()
            for ligne in data:
                print(*ligne)

            print("\n *** Header ***")
            header = file.getheader()
            print(header)
        else:
            print("File is corrupted")

    print("*** Bad file ***")
    with CsvReader('bad.csv') as file:
        if file == None:
            print("File is corrupted")

    print("*** not found file ***")
    with CsvReader('notfound.csv') as file:
        if file != None:
            data = file.getheader()