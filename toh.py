import numpy as np
class ExpectedException(Exception):
	pass
class TowersOfHanoi(object):
	NUMBER_OF_STACKS = 3
	@staticmethod
	def _initiate_towers(number_of_discs):
		towers = np.zeros((NUMBER_OF_STACKS, number_of_discs))
		for i in range(1, number_of_discs+1):
			towers[0][towers.shape[1]-i] = i
		return towers

	def __init__(self, number_of_discs):
		self.towers = TowersOfHanoi._initiate_towers(number_of_discs)
		self.numberOfDiscs = number_of_discs
		self.solveSteps = 0
		self.availableStacks = {}
		self.lastDiscSize = 0
		self.lastDiscPosition = 0

	def solved(self):
		if self.towers[NUMBER_OF_STACKS-1][number_of_discs-1] == 1:
			return True
		else:
			return False

	def reset_available_stacks(self):
		for i in range(1,NUMBER_OF_STACKS+1):
			self.availableStacks[i] = True

	def is_stack_available(self):
		stacks_available = False
		for i in range(NUMBER_OF_STACKS):
			stacks_available = self.availableStacks[i]
		return stacks_available

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

	def move(self, disc_position, disc_destination):
		if disc_destination == self.lastDiscPosition and disc_size == self.lastDiscSize:
			raise ExpectedException('previous move reversed')
		else:
			disc_size = self.towers[disc_position[0]][disc_position[1]]
			self.towers[disc_position[0]][disc_position[1]] = 0
			self.towers[disc_destination[0]][disc_destination[1]] = disc_size


	def find_greatest_disc(self, stack_status):
		"""returns tuple of greatest disc position, array of stack number and height, and greatest disc size"""
		greatest_disc_size = 0
		greatest_disc_position = np.empty(2)
		for stack_number in range(NUMBER_OF_STACKS):
			if self.availableStacks[i]:
				current_disc_size = stack_status[stack_number][1]
				if current_disc_size > greatest_disc_size:
					greatest_disc_size = current_disc_size
					greatest_disc_position[0] = stack_number
			else:
				continue
		self.availableStacks[greatest_disc_position[0]] = False
		greatest_disc_position[1] = stack_status[greatest_disc_position[0]][0]
		return greatest_disc_position, greatest_disc_size

	def find_smallest_disc(self, stack_status):
		"""returns tuple of smallest disc position, array of stack number and height, and smallest disc size"""
		smallest_disc_size = self.numberOfDiscs
		smallest_disc_position = np.empty(2)
		for stack_number in range(NUMBER_OF_STACKS):
			if self.availableStacks[i]:
				current_disc_size = stack_status[stack_number][1]
				if current_disc_size < smallest_disc_size:
					smallest_disc_size = current_disc_size
					smallest_disc_position[0] = stack_number
			else:
				continue
		self.availableStacks[smallest_disc_position[0]] = False
		smallest_disc_position[1] = stack_status[smallest_disc_position[0]][0]
		return smallest_disc_position, smallest_disc_size

	def find_right_most(self, stack_status, disc_size, stack_number):
		if stack_number < NUMBER_OF_STACKS:
			right_most_stack = 0
			for i in range(stack_number, NUMBER_OF_STACKS+1):
				if stack_status[i][1] < disc_size:
					right_most_stack = i
			if right_most_stack != 0:
				return right_most_stack
			else:
				raise ExpectedException('no available stack on the right')
		else:
			raise ExpectedException('current stack is right most stack')

	def move_greatest(self):
		stack_status = self.get_stack_status()
		while self.is_stack_available():
			greatest_disc_position, greatest_disc_size = self.find_greatest_disc(stack_status)
			try:
				next_stack_number = self.find_right_most(stack_status, greatest_disc_size, greatest_disc_position[])
				next_position = np.empty(2)
				next_position[0] = next_stack_number
				next_position[1] = stack_status[stack_number][0]
				try:
					move(greatest_disc_position, next_position)
					return True
				except ExpectedException:
					continue
			except ExpectedException:
				continue
		return False

	def move_smallest(self):
		stack_status = self.get_stack_status()
		while self.is_stack_available():
			smallest_disc_position, smallest_disc_size = self.find_smallest_disc(stack_status)
			next_position = np.empty(2)
			if smallest_disc_position < 0: #TODO: shit!!!!
				next_position[0] = smallest_disc_position[0]-1
				while next_position[0] > 0:
					next_position[1] = stack_status[next_position[0]][0]+1
					try:
						move(smallest_disc_position, next_position)
					except ExpectedException:
						next_position[0] -= 1
						continue
			else:
				continue


	def solve(self):
		if self.solved():
			return 'SOLVED'
		else:
			self.reset_available_stacks()
			if self.move_greatest():
				self.solve()
			self.reset_available_stacks()
			if self.move_smallest():
				self.solve()
			else:
				return 'ERROR'

	def __str__(self):
		return self.towers



