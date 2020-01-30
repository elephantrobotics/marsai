# Copyright (c) 2019 Elephant Robotics, Inc. All rights reserved.
# File name: 	pythonapi.py
# Author:		Leonid, Joey
# Version:		1.01			
# Date:			20, Jan, 2020
# Description:	python api to microcontroller 
# Using this MarsAI source code is subject to the terms and conditions 
# of Apache 2.0 License. Check LICENSE for more information

from pyfirmata.pyfirmata import Arduino, util
import time

mars = Arduino('/dev/ttyUSB0')

import numpy as np

while True:
	input_data = raw_input("Enter a number 1~7  for testing: ")

	# Run
	if input_data == '1':	
		mars.setRun(1)		# setRun(speed): speed 0 ~ 100%(1)
		time.sleep(3)
		mars.setRun(1)

	# Walk
	elif input_data == '2':	
		mars.setWalk(1)		# setWalk(speed): speed 0 ~ 100%(1)
		time.sleep(3)
		mars.setWalk(0.2)

	# Turn
	elif input_data == '3':	
		mars.setTurn(1, 1)	# setTurn(direction speed): direction 0/1; speed 0 ~ 100%(1)
		time.sleep(3)
		mars.setTurn(0, 1)
		time.sleep(3)
		mars.setTurn(0,0.2)

	# Set initial gait
	elif input_data == '4':	# Set initial gait
		mars.setIniGait(0,1)	# setIniGait(mode speed)
		# mode 0,1,2,3 for first value : run/ turn/ walk/ balance mode
		# speed 0 ~ 100%(1)
		time.sleep(3)
		mars.setIniGait(3,0.3)	
		time.sleep(3)

	# Set leg Angle for testing
	elif input_data == '5': # Set leg Angle
		mars.setLegAngle(1,2,-21.65,1)	# setLegAngle(legno, servono, angles, speed) 
		time.sleep(3)
		mars.setLegAngle(1,2,21.65,0.5)

	# Random move head
	elif input_data == '6':
		while True:
			rand_gau = np.random.normal(0,1)	## 68% in 1; 95% in 2
			rand_gau_2 = np.random.normal(0,2)
			rand_speed = np.random.random()*0.6
			rand_time = abs(np.random.normal(0,2)) * 3

			head_1_angle = rand_gau*10 + 10
			head_2_angle = rand_gau_2*10 - 10

			mars.setHeadAngle(1,head_1_angle,rand_speed)
			mars.setHeadAngle(2,head_2_angle,rand_speed)

			time.sleep(rand_time)

	# get leg Angle
	elif input_data == '7': 
		print (mars.getLegAngle(1,2))
		pass

	else: 
		mars.setStop()		# stop all


