
elves = {}

with open("input.txt", "r") as file:
	elve_name = 1
	total_calories = 0
	for line in file:
		if line == '\n':
			elves[elve_name] = total_calories
			total_calories = 0
			elve_name = elve_name + 1
		else:
			total_calories = total_calories + int(line)

sorted_elves = dict(sorted(elves.items(), key=lambda item: item[1], reverse=True))

print(sorted_elves)

c = 0
total_cals = 0

for k in sorted_elves:
	if c < 3:
		total_cals = total_cals + sorted_elves[k]
		c = c+1
	else:
		break;

print("Total calories for first 3: " + str(total_cals))

