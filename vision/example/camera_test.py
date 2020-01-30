#!/usr/bin/env python
# encoding: utf-8


import cv2
import numpy as np
import os
import serial
from PIL import Image, ImageStat
import math
import time


class FaceTraining():
    def __init__(self):
        pass

    def brightness(self, frame_innput):
        stat = ImageStat.Stat(frame_innput)
        r, g, b = stat.mean
        brightness_result = math.sqrt(
            0.299 * (r**2) + 0.587 * (g**2) + 0.114 * (b**2))
        # small than 40 will change the real brightness

        return brightness_result

    def face_recognition(self):

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('trainer/trainer.yml')
        cascade_path = "trainer/haarcascade_frontalface_default.xml"

        face_detector = cv2.CascadeClassifier(cascade_path)

        font = cv2.FONT_HERSHEY_SIMPLEX

        cam = cv2.VideoCapture(0)
        cam.set(3, 320)  # 1280
        cam.set(4, 180)  # 720

        confidence_min = 60
        confidence_max = 100

        while True:
            ret, img = cam.read()
            img = cv2.flip(img, 0)

            frame = Image.fromarray(img).convert('RGB')

            self.brightness(frame)

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = face_detector.detectMultiScale(
                gray,
                scaleFactor=1.1,  # 1.1
                minNeighbors=3,  # 3
                minSize=(20, 20),  # 100
            )

            print('faces_count: ', len(faces))

            for (x, y, w, h) in faces:
                person_id, confidence = recognizer.predict(
                    gray[y:y + h, x:x + w])

                confidence = 200 - confidence       # simple process
                confidence = max(confidence, 0)
                confidence = min(confidence, 100)

                if confidence > confidence_min and confidence < confidence_max:
                    print (confidence)
                    print ("===")
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.putText(img, str(confidence), (x + 5, y +
                                                       h - 5), font, 1, (255, 255, 0), 1)

            cv2.imshow('camera', img)

            k = cv2.waitKey(1) & 0xff
            if k == 27:
                break

        print("\n [INFO] Exiting Program and cleanup stuff")
        cam.release()
        cv2.destroyAllWindows()
        return Image.fromarray(img).convert('RGB'), len(faces)


if __name__ == '__main__':
    face_training = FaceTraining()

    frame, faces_count = face_training.face_recognition()
