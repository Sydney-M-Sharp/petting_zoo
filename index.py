# import the python datetime module to help us create a timestamp
# from datetime import date

from slithering import Copperheads
from walking import Llamas, Goat, Alpaca
from swimming import Goldfish, Seal, Shark, Turtle, Whale


# Walking animals below:
miss_fuzz = Llamas("morning")
# ^ here i am calling the class above. When i call it it will return based on what in the init
# miss_fuzz is an object that matches the init above
miss_fuzz.name = "Miss Fuzz"
miss_fuzz.species = "Domestic llama"
# here i am setting the values for the properties above^
# this is called an instance^
larry = Goat("Larry", "Dwarf Goat", "afternoon")
roberto = Alpaca("Roberto", "Huacaya Alpaca", "midday")

# Slithering animals below:
pete = Copperheads("Pete", "Copperhead")
# here we are creating an instance the verb being to instantiate

# Swimming animals below:
jeff = Goldfish("Jeff", "Goldfish")
# here we are creating an instance the verb being to instantiate
# here i am instantiating a class
mary = Seal("Mary", "Harp seal")
harb = Shark("Harb", "Carpet shark")
terry = Turtle("Terry", "Hawksbill turtle")
betty = Whale("Betty", "Beluga whale")


print(pete.name)
print(
    f"{roberto.name} the {roberto.species} is available to pet during the {roberto.shift} shift."
)

# todo: make 15 total classes^ and instantiate each animal.designate 5 critter each to go in these areas. As you define each one, give it one of the following properties where most appropriate:
