from array import array
from FileLoader import FileLoader

loader = FileLoader()
data = loader.load("../ressources/athlete_events.csv")
loader.display(data, 4)
loader.display(data, -4)

error=[0,1,2,3]
loader.display(error, 4)
loader.display(data, "-42")
loader.display(data, "error")
loader.display(data, 42.42)
data = loader.load("nothing.csv")
data = loader.load("../ressources/empty.csv")
data = loader.load("../ressources/noData.csv")
loader.display(data, 5)
loader.display(data, -5)