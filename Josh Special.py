print("========================================================")

my_list = ["Josh", 31, "Joe", 32, "Niya", 10.4, 100, 400, 1000]
the_sum = 0
for item in my_list:
	if type(item) is int:
		the_sum = the_sum + item

print("In Summation: {}".format(the_sum))

print("========================================================")

