from pyfirmata import Arduino, util
import time

mars = Arduino('/dev/ttyUSB0')

import numpy as np


while True:
	input_data = raw_input("Enter a number 1~5 or others for testing: ")






	if input_data == '1':	# Run
		mars.setRun(1)		# setRun(speed): speed 0 ~ 100%(1)
		time.sleep(3)
		mars.setRun(0.8)
		pass	

	elif input_data == '2':	# Walk
		mars.setWalk(1)		# setWalk(speed): speed 0 ~ 100%(1)
		time.sleep(3)
		mars.setWalk(0.2)
		pass

	elif input_data == '3':	# Turn
		mars.setTurn(1, 1)	# setTurn(direction speed): direction 0/1; speed 0 ~ 100%(1)
		time.sleep(3)
		mars.setTurn(0, 1)
		time.sleep(3)
		mars.setTurn(0,0.2)
		pass

	elif input_data == '4':	# Set initial gait
		mars.setIniGait(0,1)	# setIniGait(mode speed)
		# mode 0,1,2,3 for first value : run/ turn/ walk/ balance mode
		# speed 0 ~ 100%(1)
		time.sleep(3)
		mars.setIniGait(3,0.3)	
		time.sleep(3)
		pass

	elif input_data == '5': # Set leg Angle
		mars.setLegAngle(1,2,-21.65,1)	# setLegAngle(legno, servono, angles, speed) 
		time.sleep(3)
		mars.setLegAngle(1,2,21.65,0.5)
		pass



	elif input_data == '6':
		while True:
			rand_gau = np.random.normal(0,1)	## 68% in 1; 95% in 2
			rand_gau_2 = np.random.normal(0,2)
			rand_speed = np.random.random()
			rand_time = abs(np.random.normal(0,2)) 

			head_1_angle = abs(rand_gau*10) + 20
			head_2_angle = rand_gau_2*3 

			mars.setHeadAngle(1,head_1_angle,rand_speed)
			mars.setHeadAngle(2,head_2_angle,rand_speed)

			time.sleep(rand_time)


	# start with sit watching
	elif input_data == '7':
		while True:
			rand_gau = np.random.normal(0,1)	## 68% in 1; 95% in 2
			rand_gau_2 = np.random.normal(0,2)
			

			head_1_angle = abs(rand_gau*15)+20
			head_2_angle = rand_gau_2*4 

			rand_speed = np.random.random() *0.5
			
			# bigger head 2 , shorter time
			head_2_differ = abs(head_2_angle) / 15.0	## head 2 is bigger, differ is bigger  0~3
			head_2_differ = min(head_2_differ, 1)	## 0~1   

			# change rand time
			rand_time = abs(np.random.normal(0,2)) * (2 - head_2_differ)

			mars.setHeadAngle(1,head_1_angle,rand_speed)
			mars.setHeadAngle(2,head_2_angle,rand_speed)

			time.sleep(rand_time)

	elif input_data == '8':
		print 'rx ' + str(mars.getGyrodata(1))
		print 'ry ' + str(mars.getGyrodata(0))

	elif input_data == '99': # get leg Angle
		for i in range(1,5):
			print "leg " + str(i) 
			for l in range(1,4):
				print "joint " + str(l)
				print mars.getLegAngle(i,l)
			print '---'
		#print mars.getLegAngle(1,3)
		pass
	else: 
		mars.setStop()		# stop all


