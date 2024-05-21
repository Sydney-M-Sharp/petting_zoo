# import the python datetime module to help us create a timestamp
from datetime import date

from slithering import Copperheads
from walking import Llamas
from swimming import Goldfish



miss_fuzz = Llamas()
# ^ here i am calling the class above. When i call it it will return based on what in the init 
# miss_fuzz is an object that matches the init above
miss_fuzz.name = "Miss Fuzz"
miss_fuzz.species = "domestic llama"
# here i am setting the values for the properties above^
# this is called an instance^


pete = Copperheads("Pete","copperheads")
# here we are creating an instance the verb being to instantiate



jeff = Goldfish("Jeff","Goldfish")
# here we are creating an instance the verb being to instantiate

print(pete.name)

# todo: make 15 total classes^ and instantiate each animal.designate 5 critter each to go in these areas. As you define each one, give it one of the following properties where most appropriate: