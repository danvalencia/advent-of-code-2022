import functools

input = [
	# 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
	# 'ttgJtRGJQctTZtZT',
	# 'CrZsJsPPZsGzwwsLwLmpwMDw',
	'vJrwpWtwJgWrhcsFMMfFFhFp',
	'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
	'PmmdzqPrVvPwwTWBwg',
]

def to_rucksack(input):
	l= len(input)
	r_size = int(l/2)
	r1 = input[0:r_size]
	r2 = input[r_size:l]
	return (r1, r2)

def find_common(*rucksacks):
	sets = [set(r) for r in rucksacks]
	return functools.reduce(lambda s1, s2: s1.intersection(s2), sets)
	
def find_dupe(r1, r2):
	dupe = []
	for l in r1:
		for l2 in r2:
			if l == l2:
				dupe.append(l)
	return dupe

def find_priority(item):
	ascii = ord(item)
	if ascii >= 97:
		return ascii - 96
	else:
		return ascii - 38

p_sum = 0
with open('input.txt', 'r') as file:
	c = 0
	group = []
	for line in file:
		group.append(line.rstrip('\r\n'))
		if c == 2:
			print("c1: " + group[0])
			print("c2: " + group[1])
			print("c3: " + group[2])
			common_items = find_common(*group)
			print('Common items ' + str(common_items))
			if len(common_items) == 1:
				common_item = common_items.pop()
				p = find_priority(common_item)
				print("Common item: " + common_item + "; Priority: " + str(p))
				p_sum += p
			c = 0
			group = []
		else:
			c += 1
			

		# if len(dupe_arr) > 0:
		# 	dupe = dupe_arr[0]
		# 	p = find_priority(dupe)
		# 	p_sum += p

print(int(p_sum))

# c = find_common(*input)
# print(c)
# print(p_sum)