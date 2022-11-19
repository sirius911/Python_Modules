from game import Lannister, Stark, Targaryen

arya = Stark("Arya")
arya.print_house_words()
print(arya.is_alive)
arya.die()
print(arya.is_alive)

daenerys = Targaryen("Daenerys")
print(daenerys)

cersei = Lannister("Cersei")
cersei.die()
print (cersei.first_name)
cersei
