import re
import pathlib

stacks = []
stack_idx_line_found = False
moves = []

def convert_to_stacks(line):
	stacks_list = []
	#0,1,2,3
	next_token_idx = 0
	token_length = 4
	token_found = False
	for idx, c in enumerate(line):
		if idx == next_token_idx:
			if c == '[':
				token_found = True
			else:
				stacks_list.append(None)
				next_token_idx += token_length
		elif token_found:
			stacks_list.append(c)
			token_found = False
			next_token_idx += token_length
		
	return stacks_list
		
# stacks_line = '    [M]             [Z]     [V]    '
# print(convert_to_stacks(stacks_line))

# # cwd = pathlib.Path(__file__).parent.resolve()
# print(cwd)
# 
# Convert:
# [
# 	[None, 'M', None, None, None, 'Z', None, 'V', None], 
# 	[None, 'Z', None, 'P', None, 'L', None, 'Z', 'J'], 
# 	['S', 'D', None, 'W', None, 'W', None, 'H', 'Q'], 
# 	['P', 'V', 'N', 'D', None, 'P', None, 'C', 'V'], 
# 	['H', 'B', 'J', 'V', 'B', 'M', None, 'N', 'P'], 
# 	['V', 'F', 'L', 'Z', 'C', 'S', 'P', 'S', 'G'], 
# 	['F', 'J', 'M', 'G', 'R', 'R', 'H', 'R', 'L'], 
# 	['G', 'G', 'G', 'N', 'V', 'V', 'T', 'Q', 'F']
# ]
#
# Into this:
#
#     [M]             [Z]     [V]    
#     [Z]     [P]     [L]     [Z] [J]
# [S] [D]     [W]     [W]     [H] [Q]
# [P] [V] [N] [D]     [P]     [C] [V]
# [H] [B] [J] [V] [B] [M]     [N] [P]
# [V] [F] [L] [Z] [C] [S] [P] [S] [G]
# [F] [J] [M] [G] [R] [R] [H] [R] [L]
# [G] [G] [G] [N] [V] [V] [T] [Q] [F]
#  1   2   3   4   5   6   7   8   9 

# move = (6,9,3)
#
#
#         [L]
#         [G]
#         [P]
#     [M] [V]         [Z]     [V]    
#     [Z] [Q] [P]     [L]     [Z] 
# [S] [D] [J] [W]     [W]     [H] 
# [P] [V] [N] [D]     [P]     [C] 
# [H] [B] [J] [V] [B] [M]     [N] 
# [V] [F] [L] [Z] [C] [S] [P] [S] 
# [F] [J] [M] [G] [R] [R] [H] [R] 
# [G] [G] [G] [N] [V] [V] [T] [Q] [F]
#  1   2   3   4   5   6   7   8   9 

def map_to_stack_list(arr_list):
	stack_count = len(arr_list[0])
	stack_list = []

	stack = []
	for i in range(stack_count):
		for row in reversed(arr_list):
			if row[i]:
				stack.append(row[i])
		
		stack_list.append(stack)
		stack = []
	
	return stack_list

def apply_move(stacks, move):
	crate_count, from_stack_idx, to_stack_idx = move
	
	from_stack = stacks[from_stack_idx - 1]
	to_stack = stacks[to_stack_idx - 1]

	for n in range(crate_count):
		crate = from_stack.pop()
		to_stack.append(crate)

def apply_move_in_bulk(stacks, move):
	crate_count, from_stack_idx, to_stack_idx = move
	
	from_stack = stacks[from_stack_idx - 1]
	to_stack = stacks[to_stack_idx - 1]

	for n in range(len(from_stack) - crate_count, len(from_stack)):
		to_stack.append(from_stack[n])

	for n in range(crate_count):
		from_stack.pop()

with open(pathlib.Path(__file__).parent.joinpath('input.txt'), 'r') as file:
	for line in file:
		if re.match(r" \d.*", line):
			idx = line.split()
			stack_idx_line_found = True
		elif not stack_idx_line_found:
			stacks.append(convert_to_stacks(line))
		elif m := re.match(r"move (\d+) from (\d+) to (\d+)", line):
			move = [int(c) for c in m.groups()]
			moves.append(move)
		else:
			print("Ignoring line: " + line)

stack_list = map_to_stack_list(stacks)
move = [6,9,3]

print(stack_list)

# apply_move_in_bulk(stack_list, move)
for move in moves:
	apply_move_in_bulk(stack_list, move)

print("After applying move: ")
print(stack_list)

print("last elements:")

result = ""
for s in stack_list:
	last = s[-1]
	result += last

print(result)
# print(stacks[0:])
# print(moves)

			


