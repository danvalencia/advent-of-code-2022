import pathlib
import functools

grid = """303
255
653
"""

def calc_highest_scenic_score(grid):
	rows = len(grid)
	cols = len(grid[0])

	# [[3, 0, 3, 7, 3], 
	#  [2, 5, 5, 1, 2], 
	#  [6, 5, 3, 3, 2], 
	#  [3, 3, 5, 4, 9], 
	#  [3, 5, 3, 9, 0]]

	highest_scenic_score = 0
	for x in range(0, cols):
		for y in range(0, rows):
			curr_tree = grid[y][x]
			score = calc_scenic_score(grid, x, y)
			print("New scenic score: " + str(score) + "; Highest scenic score: " + str(highest_scenic_score))
			highest_scenic_score = max(score, highest_scenic_score)

	print(grid)
	return highest_scenic_score


def calc_scenic_score(grid, x, y):
	rows = len(grid)
	cols = len(grid[0])
	curr_tree = grid[y][x]

	# [[3, 0, 3, 7, 3], 
	#  [2, 5, 5, 1, 2], 
	#  [6, 5, 3, 3, 2], 
	#  [3, 3, 5, 4, 9], 
	#  [3, 5, 3, 9, 0]]

	print("Curr tree(" + str(x) + "," + str(y) + ") = " + str(curr_tree))

	# Find view distance on the left
	left_view_dist = 0
	for left_range in reversed(range(0, x)):
		left_view_dist += 1
		left_tree = grid[y][left_range]
		if(curr_tree <= left_tree):
			break;
	
	right_view_dist = 0
	for right_range in range(x + 1, cols):
		right_view_dist += 1
		right_tree = grid[y][right_range]
		if(curr_tree <= right_tree):
			break;

	top_view_dist = 0
	for top_range in reversed(range(0, y)):
		top_view_dist += 1
		top_tree = grid[top_range][x]
		if(curr_tree <= top_tree):
			break;

	bottom_view_dist = 0
	for bottom_range in range(y + 1, rows):
		bottom_view_dist += 1
		bottom_tree = grid[bottom_range][x]
		if(curr_tree <= bottom_tree):
			break;

	print("Left view distance: " + str(left_view_dist))
	print("Right view distance: " + str(right_view_dist))
	print("Top view distance: " + str(top_view_dist))
	print("Bottom view distance: " + str(bottom_view_dist))

	scenic_score = left_view_dist * right_view_dist * top_view_dist * bottom_view_dist
	return scenic_score

	# for right_range in range(x + 1, cols):
	# 	right_tree = grid[y][right_range]
	# 	if(curr_tree <= right_tree):
	# 		print("Right tree: " + str(right_tree) + " blocks visibility")
	# 		results.append(False)
	# 		break;
	
	# for top_range in range(0, y):
	# 	top_tree = grid[top_range][x]
	# 	if(curr_tree <= top_tree):
	# 		print("Top tree: " + str(top_tree) + "; blocks visibility")
	# 		results.append(False)
	# 		break;

	# for bottom_range in range(y + 1, rows):
	# 	bottom_tree = grid[bottom_range][x]
	# 	if(curr_tree <= bottom_tree):
	# 		print("Bottom tree: " + str(bottom_tree) + "; blocks visibility")
	# 		results.append(False)
	# 		break;
	
	# res = len(results) < 4
	# print("Curr tree(" + str(x) + "," + str(y) + ") = " + str(curr_tree) + "Is visible: " + str(res))
	# return  res

def is_tree_visible(grid, x, y):
	rows = len(grid)
	cols = len(grid[0])
	curr_tree = grid[y][x]

	results = []
	print("Curr tree(" + str(x) + "," + str(y) + ") = " + str(curr_tree))

	for left_range in range(0, x):
		left_tree = grid[y][left_range]
		if(curr_tree <= left_tree):
			print("Left tree: " + str(left_tree) + " blocks visibility")
			results.append(False)
			break;

	for right_range in range(x + 1, cols):
		right_tree = grid[y][right_range]
		if(curr_tree <= right_tree):
			print("Right tree: " + str(right_tree) + " blocks visibility")
			results.append(False)
			break;
	
	for top_range in range(0, y):
		top_tree = grid[top_range][x]
		if(curr_tree <= top_tree):
			print("Top tree: " + str(top_tree) + "; blocks visibility")
			results.append(False)
			break;

	for bottom_range in range(y + 1, rows):
		bottom_tree = grid[bottom_range][x]
		if(curr_tree <= bottom_tree):
			print("Bottom tree: " + str(bottom_tree) + "; blocks visibility")
			results.append(False)
			break;
	
	res = len(results) < 4
	print("Curr tree(" + str(x) + "," + str(y) + ") = " + str(curr_tree) + "Is visible: " + str(res))
	return  res

def find_visible_trees(grid):
	rows = len(grid)
	cols = len(grid[0])

	visible_trees = (2 * rows) + ((cols - 2) * 2)
	print("Initial Visible Trees: " + str(visible_trees))

	for x in range(1, cols - 1):
		for y in range(1, rows - 1):
			curr_tree = grid[y][x]
			is_visible = is_tree_visible(grid, x, y)
			print("Result: " + str(is_visible))
			if is_visible:
				visible_trees += 1
				print("Visible tree count: " + str(visible_trees))

	print(grid)
	return visible_trees

grid = []
with open(pathlib.Path(__file__).parent.joinpath("input.txt"), "r") as file:
	for line in file:
		row = []
		for tree_height in line.strip():
			row.append(int(tree_height))
		grid.append(row)

highest_scenic_score = calc_highest_scenic_score(grid)
print("Highest scenic score: " + str(highest_scenic_score))

# visible_trees = find_visible_trees(grid)
# print("Visible trees: " + str(visible_trees))




