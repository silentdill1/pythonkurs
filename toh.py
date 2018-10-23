import numpy as np
class TowersOfHanoi(object):
	NUMBER_OF_STACKS = 3
	@staticmethod
	def initiate_towers(number_of_discs):
		towers = np.zeros((NUMBER_OF_STACKS, number_of_discs))
		for i in range(1, number_of_discs+1):
			towers[0][towers.shape[1]-i] = i
		return towers

	def __init__(self, number_of_discs):
		self.towers = TowersOfHanoi.initiate_towers(number_of_discs)
		self.numberOfDiscs = number_of_discs
		self.solveSteps = 0

	def solved(self):
		if self.towers[NUMBER_OF_STACKS-1][number_of_discs-1] == 1:
			return True
		else:
			return False

	def get_stack_status(self):
		"""returns a array of arrays for each stack, consisting of 
		highest occupied index and size of the occupying disc"""
		stack_status = np.zeros((NUMBER_OF_STACKS, 2))
		for stack_number in range(NUMBER_OF_STACKS):
			current_stack = self.tower[stack_number]
			for disc_index in range(len(stack)-1, -1, -1):
				if current_stack[disc_index] != 0:
					stack_status[stack_number][0] = disc_index
					stack_status[stack_number][1] = current_stack[disc_index]
		return stack_status

	def move(self, disc_position):
		disc_size = self.towers[disc_position[0]][disc_position[1]]


	def solve(self):
		if self.solved():
			return 'SOLVED'
		else:
			stack_index = 0
			for 



