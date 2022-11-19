import sys
from FileLoader import FileLoader
from ProportionBySport import proportion_by_sport

loader = FileLoader()
data = loader.load("../ressources/athlete_events.csv")

green = '\033[92m'
reset = '\033[0m'
red = '\033[91m'
if len(sys.argv) == 4:
    year = int(sys.argv[1])
    sport = sys.argv[2]
    gender = sys.argv[3]
else:
    gender = 'F'
    sport = 'Tennis'
    year = 2004
    print("Usage:\n\t test.py [YEAR] [SPORT] [F/M]")

gender_text = 'Female' if gender == 'F' else 'Male'
pro = proportion_by_sport(data, year, sport, gender)
print(pro)
print(f"The percentage of {green}{gender_text} {sport}{reset} players among all the {green}{gender_text}{reset} participants of the {green}{year}{reset} Olympics is {red}{pro * 100: 0.2f}{reset}%")