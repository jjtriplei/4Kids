print("========================================================")

x = 45
y = 80
while x < 50 and y < 100:
	x = x + 1
	y = y + 1
	print(x, y)

print("========================================================")

for x in range(0, 20):
	print('hello %s' % x)
	if x == 9:
		break

print("========================================================")

for age in range(2,33,2):
	print(age)

print("========================================================")

ingredients = ["Cheese","Olives","Onions","Turkey","Spinach"]
num = 1
for i in ingredients:
	print("{} {}".format(num, i))
	num = num +1

print("========================================================")

earth_weight = 216.9
for year in range(1,16):
	moon_weight = earth_weight * .165
	print("Year: {} Weight: {}" .format(year,moon_weight))
	earth_weight = earth_weight + 2.2

print("========================================================")

