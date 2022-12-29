from enum import Enum
import logging

LOSS = 0
DRAW = 3
WIN = 6

class Outcome(Enum):
	LOSS = 0
	DRAW = 3
	WIN = 6

	@classmethod
	def from_l(cls, outcome):
		if outcome == 'X':
			return Outcome.LOSS
		elif outcome == 'Y':
			return Outcome.DRAW
		else:
			return Outcome.WIN

class Move(Enum):
	Rock = 1
	Paper = 2
	Scissors = 3

	def __str__(self):
		if self is Move.Rock:
			msg = '🪨'
		elif self is Move.Paper:
			msg = '📄'
		else:
			msg = '✄'
		return msg

	@classmethod
	def from_l(cls, move):
		if move == 'A':
			return Move.Rock
		elif move == 'B':
			return Move.Paper
		else:
			return Move.Scissors

	def from_outcome(other, outcome):
		if outcome is Outcome.LOSS:
			if other is Move.Rock:
				return Move.Scissors
			elif other is Move.Scissors:
				return Move.Paper
			else:
				return Move.Rock
		elif outcome is Outcome.WIN:
			if other is Move.Rock:
				return Move.Paper
			elif other is Move.Scissors:
				return Move.Rock
			else:
				return Move.Scissors
		else:
			return other

	def play(self, move2):
		if self is Move.Rock:
			if move2 is Move.Scissors:
				result = WIN
			elif move2 is Move.Rock:
				result = DRAW
			else:
				result = LOSS
		elif self is Move.Paper:
			if move2 is Move.Scissors:
				result = LOSS
			elif move2 is Move.Rock:
				result = WIN
			else:
				result = DRAW
		elif self is Move.Scissors:
			if move2 is Move.Scissors:
				result = DRAW
			elif move2 is Move.Rock:
				result = LOSS
			else:
				result = WIN
		
		print('Result for (' + str(self) + '  x ' + str(move2) + ' ) = ' + str(result))
		return result

my_score = 0

with open('strategy.txt', 'r') as file:
	for line in file:
		[opp_mv_l, outcome_l] = line.split()
		opp_mv = Move.from_l(opp_mv_l)
		my_mv = opp_mv.from_outcome(Outcome.from_l(outcome_l))
		result = my_mv.play(opp_mv)
		print("Result: " + str(result) + "; " + str(my_mv.value))
		my_score += (my_mv.value + result)

print('Total Score: ' + str(my_score))

r1 = Move.from_l('A')
r2 = Move.from_l('X')
p1 = Move.from_l('B')
p2 = Move.from_l('Y')
s1 = Move.from_l('C')
s2 = Move.from_l('Z')
r1.play(s2)
s2.play(r1)
r1.play(p1)
p1.play(r1)
s1.play(p1)
p1.play(s1)
r1.play(r2)
r2.play(r1)
p1.play(p2)
p2.play(p1)
s1.play(s2)
s2.play(s1)

# print(Move.from_l('A'))
# print(Move.from_l('B'))
# print(opp_move('C'))
		

