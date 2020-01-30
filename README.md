<!--
Copyright (c) 2019 Elephant Robotics, Inc. All rights reserved.

Using this MarsAI source code is subject to the terms and conditions of Apache 2.0 License. Check LICENSE for more information
-->

# MarsAI | The Artificial Intelligence for MarsCat

This is the source code for MarsCat AI. The robotic pet cat that you can control, program and pet. The goal of this AI is to gather people's knowledge to create a smart creature ever. 

## Structure 

This source code consists of:
 * **ai**: including action(eyedisplay, sound, movements), ai and data receiver from different sensors, vision and voice
 * **sensor**: touch sensor, distance sensor and gyro sensor
 * **vision**: human_recognition, object_recognition, brightness and QR code recognition
 * **voice**: command recognition
 * **library**: python API to control marscat move

## AI

The marsAI is based on general AI process flow:
 * **sense** : sense the data from environment, the RGB data, the distance, the sound wave. 
 * **feature** : transfer and abstract the sense data from raw-data to features, like RGB image data to Human faces, objects.
 * **model** : Different features may come at the same time, so sort the feature into a certain model like being-touched, start-listen and other 3 models.
 * **behaviour** : Generate the right behaviour from model to behaviour based on energy consumption, last behaviour and other information.
 * **action** : The action from the behaviour, which may includes sound, body movement and eye-display.

# Code

All code is programmed by Python 3.6. If only python API is used to control MarsCat run, walk, turn and each joint's angle, then python 2.7 and python 3 both can be used. 

The code style is under [PEP 8 Style](https://www.python.org/dev/peps/pep-0008/). If you want to contribute, please code by this style.

## Platform and Environment 

All code is running in Raspberry PI B (embedded WIFI and Bluetooth). The operating system environment is [Raspbian: Kernel 4.19](https://www.raspberrypi.org/downloads/raspbian/) 

## Libraries

Pre-installed libraries includes OpenCV 3, Pocketsphinx, Pyfirmata.

# Quick start and Examples

In construction now...

# Contact

The code is managed by Elephant Robotics INC. Email support@elephantrobotics.com to get in touch with our software teamm 