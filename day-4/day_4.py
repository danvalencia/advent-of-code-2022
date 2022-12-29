pairs_str = "2-3,4-5"

class SectionRange:
	def __init__(self, from_section: int, to_section: int):
		self.from_section = from_section
		self.to_section = to_section
	
	def includes_range(self, other):
		return self.from_section <= other.from_section and self.to_section >= other.to_section
	
	# .23456789...  2-6
	# ...45678.  4-8
	
	def overlaps(self, other):
		return (other.from_section >= self.from_section and other.from_section <= self.to_section) or (other.to_section >= self.from_section and other.to_section <= self.to_section)

	def __str__(self):
		return "(" + str(self.from_section) + "," + str(self.to_section) + ")"

	@classmethod
	def from_str(cls, s: str):
		[from_section, to_section] = s.split('-')
		return SectionRange(int(from_section), int(to_section))

counter = 0
total_lines = 0
with open('input.txt', 'r') as file:
	for line in file:
		total_lines += 1
		[first_range_str, second_range_str] = line.split(',')
		# if 
		first_range = SectionRange.from_str(first_range_str)
		second_range = SectionRange.from_str(second_range_str)
		includes_range = first_range.overlaps(second_range) or second_range.overlaps(first_range)
		if includes_range:
			counter += 1
		print("first: " + str(first_range) + "; second: " + str(second_range) + "; " + str(includes_range))

print("Total including ranges: " + str(counter) + "; total_lines: " + str(total_lines))

# [r1, r2] = pairs_str.split(',')
# range_1 = SectionRange.from_str(r1)
# range_2 = SectionRange.from_str(r2)
# print(range_1.overlaps(range_2))

# print(SectionRange(2,2).overlaps(SectionRange(3,4)))
# print(SectionRange(2,2).overlaps(SectionRange(1,2)))
# print(SectionRange(2,8).overlaps(SectionRange(3,8)))
# print(SectionRange(2,7).overlaps(SectionRange(8,9)))
# print(SectionRange(5,8).overlaps(SectionRange(2,4)))
# print(SectionRange(5,8).overlaps(SectionRange(2,6)))

# b1 = range_1.includes_range(range_2)
# b2 = range_2.includes_range(range_1)
# print("B1: " + str(b1) + " B2: " + str(b2))
# section_range = []
# for section_pair in section_pairs:
# 	section_range.append(SectionRange.from_str(section_pair))

# range_1 = section_range[0]
# range_2 = section_range[1]
# includes_range = range_1.includes_range(range_2)
# print("Includes Range " + str(includes_range))
