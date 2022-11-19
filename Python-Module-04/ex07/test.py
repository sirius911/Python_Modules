from FileLoader import FileLoader
from Komparator import Komparator
loader = FileLoader()
data = loader.load('../ressources/athlete_events.csv')
try:
    komparator = Komparator(data)
    komparator.compare_box_plots('Medal', 'Age')

    komparator.density('Medal', 'Weight')

    komparator.compare_histograms('Medal', 'Height')

except Exception as e:
    print(e)