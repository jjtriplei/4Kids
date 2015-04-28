# print("========================================================")

# x = 45
# y = 80
# while x < 50 and y < 100:
# 	x = x + 1
# 	y = y + 1
# 	print(x, y)

# print("========================================================")

# for x in range(0, 20):
# 	print('hello %s' % x)
# 	if x == 9:
# 		break

# print("========================================================")

# for age in range(2,33,2):
# 	print(age)

# print("========================================================")

# ingredients = ["Cheese","Olives","Onions","Turkey","Spinach"]
# num = 1
# for i in ingredients:
# 	print("{} {}".format(num, i))
# 	num = num +1

# print("========================================================")

# earth_weight = 216.9
# for year in range(1,16):
# 	moon_weight = earth_weight * .165
# 	print("Year: {} Weight: {}" .format(year,moon_weight))
# 	earth_weight = earth_weight + 2.2

# print("========================================================")

# def spaceship_building(cans):
# 	total_cans = 0
# 	for week in range(1, 5):
# 		total_cans = total_cans + cans
# 		print('Week %s = %s cans' % (week, total_cans))

# spaceship_building(8)

# print("========================================================")

# import time

# print(time.asctime())

# print("========================================================")

# import sys
# def silly_age_joke():
# 	print("How old are you!?")
# 	age = int(sys.stdin.readline())
# 	if age >= 10 and age <= 13:
# 		print("What is 13 + 49 + 84 + 155 + 97?")
# 		print("A HEADACHE!!!")
# 	else:
# 		print("Huh?")

# silly_age_joke()
# sys.stdin.readline()

print("========================================================")

def moon_weight(weight,gain,years):
	earth_weight = int(weight)
	for year in range(1,years+1):
		moon_weight = earth_weight * .165
		print("Year {}, weight {}".format(year,moon_weight))
		earth_weight = earth_weight + gain

moon_weight(217,50,15)

print("========================================================")

# Per Josh, this is the function that will address the answer to Problem 3 for Chapter 7

import sys

def moon_weight():
	print("How much do you weigh now?")
	earth_weight = int(sys.stdin.readline())
	print("How much are you gaining a year?")
	gain = int(sys.stdin.readline())
	print("How many years will you be coming to the moon?")
	years = int(sys.stdin.readline())

	for year in range(1,years+1):
		moon_weight = earth_weight * .165
		print("Year {}, weight {}".format(year,moon_weight))
		earth_weight = earth_weight + gain

	sys.stdin.readline()

moon_weight()

print("========================================================")