from datetime import date


class Boa:
    """Constructs a Boa"""

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
