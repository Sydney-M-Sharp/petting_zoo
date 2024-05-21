from datetime import date


class Seal:
    """constructs a seal"""

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
