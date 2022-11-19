import sys
from FileLoader import FileLoader
from HowManyMedals import how_many_medals

loader = FileLoader()
data = loader.load("../ressources/athlete_events.csv")

name = 'Kjetil Andr Aamodt'
print(len(sys.argv))
if len(sys.argv) == 2:
    name = str(sys.argv[1])
else:
    print("Usage:\n\ttest.py [NAME]")

print(how_many_medals(data, name))

# print(how_many_medals(data, "Ellina Aleksandrovna Zvereva (Kisheyeva-)"))

