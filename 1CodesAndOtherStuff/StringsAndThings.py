# Strings
#    data that falls within " "

# Concatenation
#  put 2 or more strings together

firstName = "Fred"
lastName = "Flintstone"

print(firstName + " " + lastName)

fullName = firstName + " " + lastName
print(fullName)

# Repetition
#  repetition operator: *

print("Hip "*2 + "Hooray!")

def rowYourBoat():
    print("Row, "*3 + 'your boat')
    print("Gently down the stream")
    print("Merrily, "*4)
    print("Life is but a dream")

rowYourBoat()

# Indexing

name = "Roy G Biv"
firstChar = name[0]
print(firstChar)
middleIndex = len(name) // 2
print(middleIndex)
print(name[middleIndex])


print(name[-1])

for i in range(len(name)):
    print(name[i])

# Slicing and Dicing
#   slicing operator:  :
#   slicing lets us make substrings

print(name[0:3])
print(name[:5])
print(name[6:9])
print(name[6:])

for i in range(1, len(name)):
    print(name[0:i])

# Searching inside of Strings

print("Biv" in name)
print("v" not in name)

if "y" in name:
    print("The letter y is in name")
else:
    print("The letter y is not in name")

    # String Methods to investigate:
    # Method        Use Example           Explanation
    # center        aStr.center(w)        Returns a centered string
    # ljust         aStr.ljust(w)         Returns a left justified version of the string
    # rjust         aStr.rjust(w)         Returns a right justified version of the string
    # upper         aStr.upper()          Converts a string into upper case
    # lower         aStr.lower()          Converts a string into lower case
    # index         aStr.index(item)      Searches the string for a specified value and returns the position of where it
    # was found
    # rindex        aStr.rindex(item)     Searches the string for a specified value and returns the last position of
    # where it was found
    # find          aStr.find(item)       Searches the string for a specified value and returns the position of where it
    # was found
    # rfind         aStr.rfind(item)      Searches the string for a specified value and returns the last position of
    # where it was found
    # replace       aStr.replace(old, new)  Returns a string where a specified value is replaced with a specified value

# Character Functions

print(ord('B'))

print(chr(97+13))

print(str(12548))

# testing functions from mapper.py

from mapper import *

print(letterToIndex('P'))
print(indexToLetter(10))

from Krypto import *

print(scramble2Encrypt("GOOD MORNING LADIES AND GENTLEMAN"))

print(scramble2Decrypt("ODMRIGLDE N ETEEO ONN AISADGNLMN"))
