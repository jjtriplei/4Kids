print("================================================================")
print("================================================================")

					CHAPTER 10: USEFUL PYTHON MODULES

print("================================================================")
print("================================================================")




"================================================================"
#			 Making Copies with the copy Module
"================================================================"

# Reference Chapter 8 if needed

# Animal class, with an __init__ function that takes the parameters: species, 
# number_of_legs and color.

class Animal:
	def __init__(self, species, number_of_legs, color):
		self.species = species
		self.number_of_legs = number_of_legs
		self.color = color

harry = Animal('hippogriff', 6, 'pink')

# #=================================================#

import copy
harry = Animal("hippogriff", 6, "pink")
harriet = copy.copy(harry)
print(harry.species)
# SHOULD RETURN: hippogriff
print(harriet.species)
# SHOULD ALSO RETURN: hippogriff

# #=================================================#

harry = Animal("hippogriff", 6, "pink")
carrie = Animal("chimera", 4, "green polka dots")
billy = Animal("bogill", 0, "paisley")
doomhammer = Animal("Orc", 2, "tanish")
my_animals = [harry, carrie, billy, doomhammer]
new_animals = copy.copy(my_animals)
print(new_animals[0].species)
# SHOULD RETURN: hippogriff
print(new_animals[3].species)
# SHOULD RETURN: Orc

# IF YOU CHANGE A PARAMETER of an object in an object list that has been copied, 
# the parameter changes for the copy too:

# ** Continuing above program: **

carrie.number_of_legs = 42

print(new_animals[1].number_of_legs)
# WILL RETURN: 42

# Conversely, adding new objects to the original object list, will not add those 
# objects to the copied list.

# ** Continuing above program: **

thrall = Animal("Orc", 2,"forest green")

my_animals.append(thrall)

print(len(my_animals))
# RETURNS: 5

print(len(new_animals))
# RETURNS: 4

# #=================================================#
#					DEEP COPY
# #=================================================#

# deepcopy, actually creates copies of all objects inside the object being copied.

new_animals = copy.deepcopy(my_animals)

my_animals[4].color = "deep forest pine"

print(my_animals[4].color)
# RETURNS: deep forest pine

print(new_animals[4].color)
# RETURNS: forest green

"================================================================"
					Keeping track of keywords
"================================================================"

import keyword

# iskeyword is a funtion that returns true a tring is a Python keyword
print(keyword.iskeyword('if'))
#RETURNS: True

# kwlist returns a list of Python keywords
print(keyword.kwlist)
# RETURNS: ['and', 'as', 'assert', 'break', 'class', 'continue', 'def', /
# 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', /
# 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', /
# 'return', 'try', 'while', 'with', 'yield']

"================================================================"
			Getting random numbers with the random module
"================================================================"

import random

print(random.randint(1,100))
# RETURNS RANDOM numbers

import random
num = random.randint(1, 100)
while True:
	print('Guess a number between 1 and 100')
	guess = input()
	i = int(guess)
	if i == num:
		print('You guessed right')
		break
	elif i < num:
		print('Try higher')
	elif i > num:
		print('Try lower')

