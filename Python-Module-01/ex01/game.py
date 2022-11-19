class GotCharacter:
    """Mother Class for Game of Thrones Characters Class"""

    def __init__(self, first_name = None, is_alive = True):
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to good people."""

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def die(self):
        """Character Death"""
        self.is_alive = False

    def print_house_words(self):
        """ print the words of the Character's House"""
        print (self.house_words)


class Lannister(GotCharacter):
    """A class representing the Lannister family. Or when bad things happen to good people."""

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Lannister"
        self.house_words = "Hear Me Roar!"

    def die(self):
        """Character Death"""
        self.is_alive = False

    def print_house_words(self):
        """ print the words of the Character's House"""
        print (self.house_words)


class Targaryen(GotCharacter):
    """A class representing the Targaryen family. Or when bad things happen to good people."""

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Targaryen"
        self.house_words = "Fire and Blood"

    def die(self):
        """Character Death"""
        self.is_alive = False

    def print_house_words(self):
        """ print the words of the Character's House"""
        print (self.house_words)
