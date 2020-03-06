# -*- coding: UTF-8 -*-

import math

'''
Useful Code
1, a.decreaseEnergy(b)
2, a.energyRecoverOnce()
3, a.getEnergy()
'''

class EnergyClass:
	def __init__(self):
		self.energy = 100
		self.b = -9
		self.a = 0.2
		pass

	def limitEnergy(self, _inputEnergy):
		_inputEnergy = min(100, _inputEnergy)
		_inputEnergy = max(0, _inputEnergy)
		return _inputEnergy

	def decreaseEnergy(self, d_energy):
		self.energy -= d_energy
		self.energy = self.limitEnergy(self.energy)	# ensure the energy > 0 


	def getEnergy(self):
		self.energy = self.limitEnergy(self.energy)
		return self.energy

	def energyRecoverOnce(self):
		self.energy += self.getIncreamentStep(self.energy)

	def getInverseTraj(self, input_value):
		input_value = self.limitEnergy(input_value)

		sqrtbac = math.sqrt(self.b*self.b - 4*self.a*input_value)
		x = (-self.b - sqrtbac)/(2*self.a)

		return x

	def getForwardTraj(self, input_x):
		# 20 times to recover 100
		# 10 times to recover 70
		# y = x * (-0.2x + 9)
		return input_x * (-self.a * input_x - self.b)


	def getIncreamentStep(self, input_value):
		current_x = self.getInverseTraj(input_value)

		current_x = min(19, current_x)

		next_y = self.getForwardTraj(current_x + 1)
		increa_step = next_y - input_value

		return increa_step





