from datetime import date


class Goldfish:
    """constructs a Goldfish"""

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


def __str__(self):
    return f"{self.name} is a {self.species}"
