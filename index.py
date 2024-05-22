# import the python datetime module to help us create a timestamp
# from datetime import date

from slithering import Copperhead, Boa, Cobra, Python, Viper
from walking import Llama, Goat, Alpaca, Giraffe, Camel
from swimming import Goldfish, Seal, Shark, Turtle, Whale


# --Walking animals below:--
miss_fuzz = Llama("Miss Fuzz", "Domestic llama", "morning", "Llama Chow")
# ^ here i am calling the class above. When i call it it will return based on what in the init
# miss_fuzz is an object that matches the init above
# miss_fuzz.name = "Miss Fuzz"
# miss_fuzz.species = "Domestic llama"
# here i am setting the values for the properties above^
# this is called an instance^
larry = Goat("Larry", "Dwarf Goat", "afternoon", "hay")
roberto = Alpaca("Roberto", "Huacaya Alpaca", "midday", "veggies")
mandy = Giraffe("Mandy", "Reticulated Giraffe", "morning", "carrot")
phil = Camel("Phil", "Bactrian Camel", "morning", "children")


# --Slithering animals below:--
pete = Copperhead("Pete", "Brown Copperhead")
# here we are creating an instance the verb being to instantiate
susan = Boa("Susan", "Madagascar Tree Boa")
charles = Cobra("Charles", "King Cobra")
simba = Python("Simba", "Ball Python")
judy = Viper("Judy", "Pit Viper")


# --Swimming animals below:--
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
miss_fuzz.feed()

print(miss_fuzz)