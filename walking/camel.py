from datetime import date


class Camel:
    """Constructs a Camel"""

    def ___init___(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
