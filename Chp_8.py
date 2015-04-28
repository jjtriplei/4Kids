print("================================================================")
print("================================================================")

								CLASSES

print("================================================================")
print("================================================================")

Turtle Example: 

print("================================================================")
print("================================================================")

import turtle
avery = turtle.Pen()
kate = turtle.Pen()

avery.forward(50)
avery.right(90)
avery.forward(20)

kate.left(90)
kate.forward(100)

jacob = turtle.Pen()
Jacob.left(180)
jacob.forward(80)

print("================================================================")
print("================================================================")

					Creating Classes: GIRAFFE Examples:

print("================================================================")
print("================================================================")

class Things:
	pass  # Added no attributes to the class.

class Inanimate(Things): #Created child class. "Things" is the parent class. Added no 
	pass

class Sidewalks(Inanimate): #Created child class. "Inanimate" is the parent class.
	pass

class Animate(Things):
	pass

class Animals(Animate):
	def breathe(self):
		print("Breathing")
	def move(self):
		print("Moving")
	def eat_food(self):
		print("Eating food")

class Mammals(Animals):
	def feed_young_with_milk(slef):
		print("Feeding young")

class Giraffes(Mammals):
	def eat_leaves_from_trees(self):
		# print("Eating leaves"
		self.eat_food()
	def find_food(self):
		self.move()     # This function calls another function
		print("I've found food!!!")
		self.eat_food() # This function calls another function again
	def dance_a_jig(self):
		self.move()
		self.move()
		self.move()
		self.move()

# Use this function to create an object with values called 'properties'
# The initalize function is preceeded and followed by two underscores. Python 
# will automatically call this function when we create a new object
	def __init__(self,spots): 
		self.giraffe_spots = spots # Look at Ozwald and Gertrude to see this


reginald = Giraffes() #created an object in the Giraffes class

reginald.move() #Call class functions on object. Functions from parent 
				#classes can be called
reginald.eat_leaves_from_trees()



harold = Giraffes() #created another object in the Giraffes class

harold.move() #Called function on Harold
harold.eat_leaves_from_trees()
harold.find_food()




Ozwald = Giraffes(100)
Gertrude = Giraffes(150)

print(Ozwald.giraffe_spots)
print(Gertrude.giraffe_spots)

print("================================================================")
print("================================================================")

					PROGRAMMING PUZZLES: PUZZLE ONE:

print("================================================================")
print("================================================================")

class Giraffes():
	def left_foot_forward(self):
		print("Left foot forward")
	def left_foot_back(self):
		print("Left foot back")
	def right_foot_forward(self):
		print("Right foot forward")
	def right_foot_back(self):
		print("Right foot back")
	def dance(self):
		self.left_foot_forward()
		self.left_foot_back()
		self.right_foot_forward()
		self.right_foot_back()
		self.left_foot_back()



print("================================================================")
print("================================================================")

					PROGRAMMING PUZZLES: PUZZLE TWO:

print("================================================================")
print("================================================================")

import turtle

Tom = turtle.Pen()
Dick = turtle.Pen()
Harry = turtle.Pen()
Mary = turtle.Pen()

Tom.forward(200)
Tom.left(90)
Dick.forward(200)
Dick.right(90)
Harry.forward(220)
Harry.left(90)
Mary.forward(220)
Mary.right(90)

Tom.forward(100)
Dick.forward(100)
Harry.forward(50)
Mary.forward(50)
Tom.right(90)
Dick.left(90)
Harry.right(90)
Mary.left(90)

Tom.forward(75)
Dick.forward(75)
Harry.forward(60)
Mary.forward(60)