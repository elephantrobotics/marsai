# file

import time
from VL530L0XP.python import VL53L0X

class Distance:
	def __init__(self):
		self.tof = VL53L0X.VL53L0X()
		self.tof.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)

		self.check_timming()
		self.min_dis = 100
		self.max_dis = 400
		self.na_distance = -1
		self.read_time = 0.07

	def check_timming(self):
		self.read_time = self.tof.get_timing()
		if (self.read_time < 20000):
			self.read_time = 20000
		self.read_time = self.read_time/1000000.00

	def get_distance(self):	# in mm

		dis = self.tof.get_distance()
		dis = self.verify_distance(dis)

		time.sleep(self.read_time*2)
		return dis

	def stop_reading(self):
		self.tof.stop_ranging()
		
		
	def verify_distance(self,distance):
		if distance < self.min_dis or distance > self.max_dis:
			return self.na_distance
		else:
			return distance

''' simple test sensor

if __name__ == '__main__':
	ds = Distance()
	while 1:
		print (ds.get_distance())
		time.sleep(0.1)

'''
