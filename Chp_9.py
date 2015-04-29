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

								FUNCTION 2: BOOL

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

#=================================================#
## USE:

year = input('year of birth: ')
#Will return: Year of birth:
if not bool(year.rstrip()):
	print('You need to enter a value for your year of birth')

# the if statement checks the Boolean value of the variable
# after using the rstrip function (which removes any spaces 
# and enter characters from the end of the string). If nothing
# is entered, the bool function will return 'false'

#=================================================#

print("================================================================")
print("================================================================")

								FUNCTION 3: DIR

print("================================================================")

# The dir function (short for directory) returns information 
# about any value. Basically, it tells you the functions that
# can be used with that value in alphabetical order.

dir(['a','short','list'])

dir(1)
#not very useful

popcorn = "I love popcorn!"
dir(popcorn)

# At this point, you could use help to get a short description of
# any function in the list.

help(popcorn.upper)
# PRINTS:
# Help on built-in function upper:

# upper(...)
# S.upper() -> str
# Return a copy of S converted to uppercase.

print("================================================================")
print("================================================================")

								FUNCTION 4: EVAL

print("================================================================")

# The eval function (short for evaluate) takes a string as a 
# parameter and runs it as though it were a Python expression

eval('print("WOW")') # Evaluates print("WOW")

eval('10*5')
# Will return: 50

# The eval function works only with simple expressions
# Expressions that are split over more than one line 
# (such as if statements) generally won’t evaluate

eval('''if True:
	print("this won't work at all")''')
# This returns a Syntax error

#=================================================#

# The eval function is often used to turn user input into Python
# expressions. For example, you could write a simple calculator 
# program that reads equations entered into Python and then 
# calculates (evaluates) the answers.
# Since user input is read in as a string, Python needs to convert
# it into numbers and operators before doing any calculations. The
# eval function makes that conversion easy:

your_calculation = input("Enter a Calculation: ")
# Will Return: Enter a Calculation: 
eval("your_calculation")
# Will Return calculation

print("================================================================")
print("================================================================")

								FUNCTION 5: EXEC

print("================================================================")

# The exec function is like eval, except that you can use it to run more
# complicated programs. The difference between the two is that eval
# returns a value (something that you can save in a variable), whereas
# exec does not.

my_small_program = '''print("Ham")
print("Sammich")'''
exec(my_small_program)


print("================================================================")
print("================================================================")

								FUNCTION 6,7 & 8 : FLOAT, 

print("================================================================")

float("12")
# RETURNS: 12.0
float("123.456789")
# RETURNS: 123.456789

#Practical Use:

your_age = input("Enter your Age: ")

age = float(your_age)
if age > 13:
	print("You're {}s years too old")




#=================================================#
EXAMPLE:

your_calculation = input("Enter your Calculation: ")
# RETURNS: Enter your Calculation: 12*52
eval("your_calculation")
# RETURNS: 624
#=================================================#



#=================================================#
OPENING FILES
#=================================================#
test_file = open('C:\\Users\\III\\Desktop\\Coding Lessons\\4Kids\\test.txt')
text = test_file.read()
print(text)

# On the first line, we use open, which returns a file object
# with functions for working with files. The parameter we use with
# the open function is a string telling Python where to find the file.
# The two backslashes in the Windows filename tell Python
# that the backslash is just that, and not some sort of command. (As
# you learned in Chapter 3, backslashes on their own have a special
# meaning in Python, particularly in strings.) We save the file object
# to the variable test_file.
# On the second line, we use the read function, provided by the
# file object, to read the contents of the file and store it in the variable
# text. We print the variable on the final line to display the
# contents of the file.
#=================================================#

#=================================================#
WRITING TO FILES
#=================================================#
test_file = open('C:\\Users\\III\\Desktop\\Coding Lessons\\4Kids\\testwrite.txt',"w")

# The file object returned by open has other functions besides read.
# We can create a new, empty file by using a second parameter, the
# string 'w', when we call the function.
# The parameter 'w' tells Python that we want to write to the
# file object, rather than read from it.
# We can now add information to this new file using the write
# function:

test_file = open('C:\\Users\\III\\Desktop\\Coding Lessons\\4Kids\\testwrite.txt',"w")
test_file.write("This is my test file")
test_file.close() # we need to tell Python when we’re finished writing to
# the file, using the close function:
#=================================================#
