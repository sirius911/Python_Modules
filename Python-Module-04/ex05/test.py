import sys
from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('../ressources/athlete_events.csv')

from HowManyMedalsByCountry import how_many_medals_by_country

country = 'Kenya'
if len(sys.argv) == 2:
    country = str(sys.argv[1])
else:
    print("Usage:\n\ttest.py [COUNTRY]")
print(how_many_medals_by_country(data, country))
