print("================================================================")
print("================================================================")

							BUILT-IN PYTHON FUNCTIONS

print("================================================================")
print("================================================================")

								FUNCTION 1: ABS

print("================================================================")

# abs returns "absolute" value of a number

print(abs(10))
# will return: 10
print(abs(-10))
# will return: 10

print("================================================================")

steps = -3
if abs(steps) > 0:
	print("Character is moving")

# WITHOUT ABS:

steps = -3
if steps > 0 or steps < 0:
	print("Character is moving")

# PERSONAL CEMENTING

steps = -3 # CAN EVEN USE, abs(-3) as a postive value
direction = "right"
if abs(steps) > 0
	if steps < 0:
		direction = "Left"
	print("Character is moving {} steps to the {}".format(abs(steps),direction))
else:
	print("Character is chillin'")

print("================================================================")
print("================================================================")

								FUNCTION 2: 

print("================================================================")

# The name bool is short for Boolean, the word programmers use to
# describe a type of data that can have one of two possible values,
# usually either true or false.
# The bool function takes a single parameter and returns either
# True or False based on its value.

NUMBERS:

print(bool(0))
# RETURNS "FALSE"
print(bool(1))
# RETURNS "TRUE"
print(bool(1123.23))
# RETURNS "TRUE"
print(bool(-500))
# RETURNS "TRUE"

STRINGS:

print(bool(None))
# RETURNS "FALSE"
print(bool("a"))
# RETURNS "TRUE"
print(bool(" "))
# RETURNS "TRUE"
print(bool("What do you call a pig doing katate? PORK CHOP!!"))
# RETURNS "TRUE"

LISTS, TUPLES, MAPS:

my_list = []
print(bool(my_list))
# RETURNS "FALSE"
my_list = ["l","i","s","t"]
print(bool(my_list))
# RETURNS "TRUE"

