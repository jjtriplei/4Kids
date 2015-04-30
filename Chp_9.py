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

#=================================================#
EXAMPLE:

your_calculation = input("Enter your Calculation: ")
# RETURNS: Enter your Calculation: 12*52
eval("your_calculation")
# RETURNS: 624
#=================================================#

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

FUNCTION 6,7,8,9,10,11 AND 12 : FLOAT, INT, LEN, MAX, MIN, RANGE, SUM

print("================================================================")

#=================================================#
# FLOAT
#=================================================#

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
# INT
#=================================================#


int(123.456)
# RETURNS: 123
# int will drop numbers after the decimal, but will not round up or down

int("123")
# RETURNS: 123

int("123.456")
# RETURNS VALUE ERROR BITCH!! :)

#=================================================#
# LEN
#=================================================#

# Short for length. Makes sence huh?
# Counts characters in strings
len('This is a test string')
# RETURNS: 21 
# Counts spaces

# Counts elements in lists
creature_list = ['unicorn', 'cyclops','fairy','elf','dragon','troll']
print(len(creature_list))
# RETURNS: 6

# Counts items in a map
enemies_map = {'Captain America' : 'Red Skull', 'Hank Pym' : 'Ultron'\
'Spider-man' : 'Venom', 'Thor' : 'Loki'}
print(len(enemies_map))
# RETURNS: 4

# IN A LOOP:
fruit = ['apple','banana','clementine','dragon fruit']
length = len(fruit)
for x in range(0,length):
	print('The fruit at index {} is {}'.format(x,fruit[x]))
# RETURNS:
# The fruit at index 0 is apple
# The fruit at index 1 is banana
# The fruit at index 2 is clementine
# The fruit at index 3 is dragon fruit

#=================================================#
# MAX and MIN
#=================================================#

numbers = [5,4,10,30,22]
print(max(numbers))
# RETURNS: 30

strings = 's,t,r,i,n,g,S,T,R,I,N,G'
print(max(strings))
# RETURNS: t
# letters are ranked alphabetically, and lowercase letters come 
# after uppercase letters, so t is more than T

print(max(10,300,450,50,90))
# RETURNS: 450

numbers = [5,4,10,30,22]
print(min(numbers))
# RETURNS: 4

# IN USE:
guess_this_number = 61
player_guesses = [12,15,70,45]
if max(player_guesses) > guess_this_number:
	print('Boom! You all lose')
else:
	print('You win')
# RETURNS: Boom! You all lose

#=================================================#
# RANGE
#=================================================#

for x in range(0,5):
	print(x)
# RETURNS: 
# 0
# 1
# 2
# 3
# 4

print(list(range(0,5)))
# RETURNS: [0,1,2,3,4]

count_by_twos = list(range(0,30,2))
print(count_by_twos)
# RETURNS: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

count_down_by_twos = list(range(40,10,-2))
print(count_down_by_twos)
# RETURNS: [40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12]

#=================================================#
# SUM
#=================================================#

my_list_of_numbers = list(range(0,500,50))
print(my_list_of_numbers)
# RETURNS: [0, 50, 100, 150, 200, 250, 300, 350, 400, 450]
print(sum(my_list_of_numbers))
# RETURNS: 2250


print("================================================================")
print("================================================================")

			FUNCTION 13 : WORKING WITH FILES

print("================================================================")


#=================================================#
OPENING FILES
#=================================================#
test_file = open('C:\\Users\\III\\Desktop\\Coding Lessons\\4Kids\\test.txt')
text = test_file.read()
print(text)
# 'open' returns a 'file object' with functions for working with files.
# For the parameter, use a string telling Python where to find the file.
# The two backslashes in the Windows filename tell Python
# that the backslash is just that, and not some sort of command 
# (backslashes on their own have a special meaning in Python,
# particularly in strings.) 
# The 'file object' is saved to the variable 'test_file'. The 'read' 
# function, provided by the 'file object', reads the contents of the
# file and stores it in the variable 'text'. Printing the variable will
# display the contents of the file.

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
test_file.write("This is my super cereal test file")
test_file.close() # we need to tell Python when we’re finished writing
# to the file, using the close function:
#=================================================#


print("================================================================")
print("================================================================")

					PROGRAMMING PUZZLES: PUZZLE ONE:

print("================================================================")
print("================================================================")

a = abs(10) + abs(-10)
print(a)
# WILL RETURN: 20
b = abs(-10) + -10
print(b)
# WILL RETURN: 0


print("================================================================")
print("================================================================")

					PROGRAMMING PUZZLES: PUZZLE TWO:

print("================================================================")
print("================================================================")

string = "this if is you not are a reading very this good then way you \
to have hide done a it message wrong"
string2 = string.split()
string3 = ""

for w in range(0,len(string2),2):
	string3 = string3 + " " + string2[w]
print(string3)

# #=================================================#
# 					JOSH SPECIAL:
# #=================================================#

# The pythonic way to do that is to not use range
# You're using range to get the current index during the loop
# Which is a legitimate need for this :)
# But what you'd actually wanna do is use enumerate
# for index, word in enumerate (string3):
# Index will be the number of the loop
# Word will be a word in the list of split strings
# Try it out :)
# Handy tool to have

print("================================================================")
print("================================================================")

					PROGRAMMING PUZZLES: PUZZLE THREE:

print("================================================================")
print("================================================================")

test_file = open('C:\\Users\\III\\Desktop\\Coding Lessons\\4Kids\\testwrite.txt',"w")
test_file.write("This is my super cereal test file")
test_file.close()