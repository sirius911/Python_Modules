from MyPlotLib import MyPlotLib
from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('../ressources/athlete_events.csv')
my = MyPlotLib()
features = ["Weight", "Height"]
my.histogram(data,features)
my.density(data, features)
my.pair_plot(data,features)
my.box_plot(data, features)
