import pathlib

moves = []
with open(pathlib.Path(__file__).parent.joinpath('test.txt'), 'r') as file:
	for line in file:
		m = line.strip().split()
		moves.append((m[0], int(m[1])))

h_pos = (0,0)
t_pos = (0,0)

for move in moves:
	direction = move[0]
	steps = move[1]

	for step in steps:
		if direction == 'U':
			print('Moving up one step')
		elif direction == 'R':
			print('Moving right one step')
		elif direction == 'D':
			print('Moving down one step')
		else:
			print('Moving left one step')


print(moves)