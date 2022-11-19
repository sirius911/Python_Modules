import pandas as pd

def proportion_by_sport(data, year, sport, gender):
    """
        function displaying the proportion of participants who played
        a given sport, among the participants of a given genders.
        args:
            • a pandas.DataFrame of the dataset,
            • an olympic year (integer positive),
            • a sport, (string)
            • a gender ('F' 'M').
        return:
                float

        """
    masque = "Year == "+str(year)+" and Sex == '" + gender +\
        "' and Sport == '" + sport + "'"
    nb = len(data.query(masque).drop_duplicates(subset=['Name']))
    masqueTotal = "Year == "+str(year)+" and Sex == '" + gender +"'"
    total = len(data.query(masqueTotal).drop_duplicates(subset=['Name']))
    if total != 0:
        return (nb / total)
    else:
        print("Error there is no data for the Year : {Year}")
        return 0
    