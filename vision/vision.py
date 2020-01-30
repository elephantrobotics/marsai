#!/usr/bin/env python
# encoding: utf-8

# Copyright (c) 2019 Elephant Robotics, Inc. All rights reserved.
# File name: 	vision.py
# Author:		Leonid, Joey
# Version:		1.01			
# Date:			20, Jan, 2020
# Description:	vision source code 
# Using this MarsAI source code is subject to the terms and conditions 
# of Apache 2.0 License. Check LICENSE for more information

import cv2
import numpy as np
import os

from PIL import Image, ImageStat
import math
import time
import copy

import sys
sys.path.append(".")

from ai.static_vars import static_vars
from ai import feature
from ai.feature import Feature

class Vision:
	def __init__(self):
		# face recognition
		self.recognizer = cv2.face.LBPHFaceRecognizer_create()
		self.recognizer.read('vision/trainer/trainer.yml')
		cascade_path = "vision/trainer/haarcascade_frontalface_default.xml"
		self.face_detector = cv2.CascadeClassifier(cascade_path)
		# object recognition
		self.master = []
		self.MAX_COUNT = 6
		self.min_counter_size = 500
		self.MAX_SUM = 10000  # sum area size
		self.MAX_DIS = 200   # distance between two center
		self.last_x = -1
		self.last_y = -1
		self.dis = 0
		self.counter = 0
		self.min_occupy = 0.6
		self.len_count = 20
		self.object_count = 0
		cam_width = 320
		cam_length = 160
		cam_no = 0
		self.cam = cv2.VideoCapture(cam_no)
		self.cam.set(3, cam_width) #1280
		self.cam.set(4, cam_length) #720

	@static_vars(last=0, img=None)
	def get_frame(self):
		if (time.time() - Vision.get_frame.last) > 0.2:
			Vision.get_frame.last = time.time()
			Vision.get_frame.img = cv2.flip(self.cam.read()[1], 0)
		return Vision.get_frame.img

	# Brightness: will return 0~150
	def get_brightness(self):
		# get brightness
		img = self.get_frame()
		frame = Image.fromarray(img).convert('RGB')
		stat = ImageStat.Stat(frame)
		r, g, b = stat.mean
		brightness = math.sqrt(0.299 * (r**2) + 0.587 * (g**2) + 0.114 * (b**2))
		# create feature
		ft = Feature()
		ft.type = feature.Type.Brightness.value
		ft.received_time = time.time()
		ft.timeout = 0.2
		brightness_data = {}
		brightness_data['brightness'] = brightness
		ft.data = brightness_data
		return ft

	# QR code: return qr code data
	def get_qrcode(self):
		img = self.get_frame()
		det = cv2.QRCodeDetector()
		qr_data,_,_ = det.detectAndDecode(img)
		if not qr_data:
			return None
		ft = Feature()
		ft.type = feature.Type.QRCode.value
		ft.received_time = time.time()
		ft.timeout = 1.0
		ft.data = qr_data
		return ft

	def get_moving_distance(self, input_c1, input_c2):
		x_1 = input_c1[0]
		y_1 = input_c1[1]
		x_2 = input_c2[0]
		y_2 = input_c2[1]
		return math.sqrt((x_1 - x_2)*(x_1 - x_2) + (y_1 - y_2)*(y_1 - y_2))

	# Moving object: return moving object coords
	def get_moving_object(self):
		frame0 = cv2.flip(self.cam.read()[1], 0)
		frame1 = cv2.cvtColor(frame0, cv2.COLOR_BGR2GRAY)
		frame2 = cv2.GaussianBlur(frame1, (25, 25), 0)   # 15 15
		if len(self.master) is 0:
			self.master = copy.deepcopy(frame2)
		frame3 = cv2.absdiff(self.master, frame2)
		frame4 = cv2.threshold(frame3, 15, 255, cv2.THRESH_BINARY)[1]
		kernel = np.ones((2, 2), np.uint8)
		frame5 = cv2.erode(frame4, kernel, iterations=4)
		frame5 = cv2.dilate(frame5, kernel, iterations=8)
		# find contours on thresholded image
		nada, contours, nada = cv2.findContours(frame5.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		# make coutour frame
		frame6 = frame0.copy()
		frame7 = frame0.copy()
		# target contours
		targets = []
		len_c = len(contours)
		if len_c < self.MAX_COUNT:
			# loop over the contours
			for c in contours:
				# if the contour is too small, ignore it
				if cv2.contourArea(c) > self.min_counter_size:
					# contour data
					M = cv2.moments(c)  # ;print( M )
					cx = int(M['m10'] / M['m00'])
					cy = int(M['m01'] / M['m00'])
					x, y, w, h = cv2.boundingRect(c)
					rx = x + int(w / 2)
					ry = y + int(h / 2)
					ca = cv2.contourArea(c)
					
					targets.append((cx, cy, ca))
			# make target
			mx = 0
			my = 0
			if targets:
				area = 0
				area_sum = 0
				for x, y, a in targets:
					if a > area:
						mx = x
						my = y
						area = a
						area_sum += a

			if self.last_x != -1:
				self.dis = self.get_moving_distance([mx,my],[self.last_x, self.last_y])
			if targets :

				if area_sum < self.MAX_SUM:
					if 	self.dis < self.MAX_DIS:
						cv2.circle(frame7, (mx, my), 30, (0, 0, 255, 0), 2)
						cv2.circle(frame7, (mx, my), 2, (0, 255, 0), 2)
						self.last_x = mx
						self.last_y = my
						self.object_count += 1
				else:
					self.object_count = 0
					self.counter = 0
		# update master
		self.master = frame2

		# Verify
		self.counter += 1
		if self.counter > self.len_count:
			obj_occu = self.object_count / self.len_count

			self.object_count = 0
			self.counter = 0

			if obj_occu > self.min_occupy:
				_x = copy.deepcopy(self.last_x)
				_y = copy.deepcopy(self.last_y)
				obj_coords = [float(_x), float(_y)]
				ft = Feature()
				ft.type = feature.Type.Object.value
				ft.received_time = time.time()
				ft.timeout = 1.0
				ft.data = {}
				ft.data['obj'] = [0,obj_coords]	
				return ft
		# All done 
		return None

	# still under final development 
	def get_object_recognition(self):
		img = self.get_frame()
		pass 

	# face recognition
	def get_face_recognition(self):
		# setups
		img = self.get_frame()
		font = cv2.FONT_HERSHEY_SIMPLEX
		confidence_min = 60
		confidence_max = 100
		face_data = []
		frame = Image.fromarray(img).convert('RGB')
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces = self.face_detector.detectMultiScale(
			gray,
			scaleFactor=1.1,
			minNeighbors=3, 
			minSize=(20, 20),
		)

		for (x, y, w, h) in faces:
			person_id, confidence = self.recognizer.predict(gray[y:y + h, x:x + w])			
			confidence = 200 - confidence       # simple process
			confidence = max(confidence, 0)
			confidence = min(confidence, 100)
			if confidence > confidence_min and confidence < confidence_max:
				cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
				cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)
				data = [(float(x), float(y)), confidence]
				face_data.append(data)

		if len(face_data) == 0:
			return None

		ft = Feature()
		ft.type = feature.Type.People.value
		ft.received_time = time.time()
		ft.timeout = 1.0
		ft.data = {}
		ft.data['human'] = face_data
		return ft


def test_vision(test_data):
	a = Vision()

	while True:
		cv2.imshow("img", a.get_frame())
		result = None

		# detect moving object
		if test_data == 1:
			result = a.get_moving_object()

		# detect face
		elif test_data == 2:
			result = a.get_face_recognition()

		# detect brightness
		elif test_data == 3:
			result = a.get_brightness()

		# detect qrcode
		elif test_data == 4:
			result = a.get_qrcode()

		print (result)

		k = cv2.waitKey(1) & 0xff
		if k == 27:
			break

