import math

'''
Useful Code
1, a.decrease_energy(b)
2, a.energy_recover_once()
3, a.get_energy()
'''

class EnergyPlanner:
    def __init__(self):
        self.energy = 100
        self.b = -9
        self.a = 0.2

    def limit_energy(self, _inputEnergy):
        _inputEnergy = min(100, _inputEnergy)
        _inputEnergy = max(0, _inputEnergy)
        return _inputEnergy

    def decrease_energy(self, d_energy):
        self.energy -= d_energy
        self.energy = self.limit_energy(self.energy)    # ensure the energy > 0 

    def get_energy(self):
        self.energy = self.limit_energy(self.energy)
        return self.energy

    def energy_recover_once(self):
        self.energy += self.get_increment_step(self.energy)

    def get_inverse_traj(self, input_value):
        input_value = self.limit_energy(input_value)

        sqrtbac = math.sqrt(self.b*self.b - 4*self.a*input_value)
        x = (-self.b - sqrtbac)/(2*self.a)

        return x

    def get_forward_traj(self, input_x):
        # 20 times to recover 100
        # 10 times to recover 70
        # y = x * (-0.2x + 9)
        return input_x * (-self.a * input_x - self.b)

    def get_increment_step(self, input_value):
        current_x = self.get_inverse_traj(input_value)

        current_x = min(19, current_x)

        next_y = self.get_forward_traj(current_x + 1)
        increa_step = next_y - input_value

        return increa_step
