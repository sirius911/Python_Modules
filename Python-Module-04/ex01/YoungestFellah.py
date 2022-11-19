import pandas as pd

def youngest_fellah(data, year):
    """
     return a dictionary containing
        the age of the youngest woman and the youngest man who took
        part in the Olympics a given year.
    args:
        data: a panda.DataFrame which contains the dataset
        year: a Olympic year ( integer)

    return:
        a dictionary

    """
    if isinstance(data, pd.DataFrame):
        try:
            if int(year) == year:
                if year >= 0:
                    dict_return = {}
                    masqueF = "Year == " + str(year) + " and Sex == 'F'"
                    masqueM = "Year == " + str(year) + " and Sex == 'M'"
                    dict_return["F"] = data.query(masqueF).Age.min()
                    dict_return["M"] = data.query(masqueM).Age.min()
                    return dict_return
                else:
                    print("Error: year must be a positive integer")
            else:
                print("Error: year must be an integer.")
        except Exception as e:
            print(e)
            print("Error: year must be an integer.")
    return None
