from datetime import date


class Llama:
    """Constructs a Llama"""

    def __init__(self, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True
        self.shift = shift


# when this is called^ provide a name species and a date
