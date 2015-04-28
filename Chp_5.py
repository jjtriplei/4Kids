print("========================================================")

print("Puzzle 2")

twinkies = None
if twinkies < 100 and twinkies > 0:
	print("Too few Twinkies.")
elif twinkies > 500:
	print("Alright already! That's too many Twinkies!")
else:
	print("Twinkies?")

print("========================================================")

print("Puzzle 3")

money_3 = None
if money_3 >=100 and money_3 <= 500:
	print("It's inbetween $100 and $500.")
elif money_3 >= 1000 and money_3 <= 5000:
	print("Whoa, there's gotta be somewhere between a G and 5 Gs here!")
else:
	print("Money?")

print("========================================================")

print("Puzzle 4")

ninjas = 49
if ninjas < 50 and ninjas > 30:
	print("Well shit. That's too many damn ninjas.")
elif ninjas <= 30 and ninjas > 10:
	print("It'll be a struggle, but I can take 'em!")
elif ninjas <= 10:
	print("I'ma fuck these ninjas up.")

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