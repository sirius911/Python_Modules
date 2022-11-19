import sys
from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('../ressources/athlete_events.csv')

from SpatioTemporalData import SpatioTemporalData
sp = SpatioTemporalData(data)

if len(sys.argv) == 3:
    func = str(sys.argv[1])
    var = sys.argv[2]
    if func not in ['where', 'when']:
        print("Error of function (where or when")
        quit()
    if func == 'where':
        city = sp.where(int(var))
        if len(city) == 0:
            print(f"No Olympic competitions in {var}")
        else:
            print(city)
    else:
        year = sp.when(var)
        if len(year) == 0:
            print(f"No Olympic competitions at {var}")
        else:
            print(sp.when(var))
else:
    print("Usage:\n\ttest.py [where/when] [YEAR/CITY]")
    print(sp.where(1896))

    print(sp.where(2016))

    print(sp.when('Athina'))

    print(sp.when('Paris'))

    print(sp.where(1895))

    print(sp.when('Sanihac'))