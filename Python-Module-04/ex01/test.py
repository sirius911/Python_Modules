from json import load
import sys
from FileLoader import FileLoader
from YoungestFellah import youngest_fellah

loader = FileLoader()
data = loader.load("../ressources/athlete_events.csv")

if len(sys.argv) == 2:
    year = int(sys.argv[1])
else:
    year = 2004
    print("Usage:\n\ttest.py [YEAR]")

print(youngest_fellah(data, year))