x = "There are %d types of people." % 10
binary = "binary"
doNot = "don't"
y = "Those who know %s and those who %s" % (binary, doNot)

print(x)
print(y)

print("I said: %r" % x)
print("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)


# More Stuff

print("Mary had a little lamb.")
print("Its fleece was white as %s." % 'snow')
print("And everywhere that Mary went.")
print("." * 10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 +end4 + end5 + end6 + end7 + end8 + end9 + end10 + end11 + end12)

# More Formatting
formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % ("One", "two", "three", "four"))
print(formatter % (True, False, False,True))
print(formatter % (formatter, formatter, formatter,formatter))

# Why did I use %r instead of %s?

print("We have already used the %s and since it is a new section, we need to use a new letter")

Fe1 = "D"
Fe2 = "i"
Fe3 = "v"
Fe4 = "i"
Fe5 = "n"
Fe6 = "g"

print(Fe1 + Fe2 + Fe3 + Fe4 + Fe5 + Fe6)

# Time for some strange stuff in the world of printing...

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Ja\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)

print("""
There's something going on here.
With the double quotes
I'll be able to type as much as we like.
Even 4 lines or more.
""")

#What if I didn't like Jan being listed on the line with the rest of the
# text and away from the other months? How could I fix that?

# More escaping

tabbyDog = "\tI'm tabbed in."
persianDog = "I'm split\non a line."
backslashDog = "I'm \\ a \\ cat."
taskDog = """
I'll make a list:
\t* Dog food
\t* Fishies
\t* Dog\n\tWater
"""

print(tabbyDog)
print(persianDog)
print(backslashDog)
print(taskDog)

#Esacpe seq           what does it do?
# \\                   Spaces out words
# \'
# \"
# \a
# \b
# \f
# \n
# \N(name)
# \r
# \t                   Makes tabbing space between charcters
# \uxxxx
# \Uxxxxxxxx
# \v
# \ooo
# \xhh
# What does the following code do:
# while true
#      for i in ["/","-","|","\\","|"}:
#          print("%s\r" % i, end='')

# Can you replace """ with '''?


# Asking Questions

age = input("How old are you?")
height = input("How tall are you?")

print("So, you really %r old and %r tall? Wow..." % (age, height))


weight = input("How much do you weigh?")

print("You weigh %s pounds? That's cool dude..." % weight)




