#!/usr/bin/env python
# encoding: utf-8

# Copyright (c) 2019 Elephant Robotics, Inc. All rights reserved.
# File name:    touch.py
# Author:       Leonid, Joey
# Version:      1.01
# Date:         20, Jan, 2020
# Description:  touch sensor source code
# Using this MarsAI source code is subject to the terms and conditions
# of Apache 2.0 License. Check LICENSE for more information

import RPi.GPIO as GPIO
import time

class Touch:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.IOlist = [4, 23, 24, 16, 20, 21]
        self.IOValue = [[0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0]]

        self.final_value = [0, 0, 0, 0, 0, 0]
        self.valuenum = 0

        self.count_data = [0, 0, 0, 0, 0, 0]

        self.max_count = 25

        for i in range(6):
            GPIO.setup(self.IOlist[i], GPIO.IN)

    def get_touch(self):
        # for group_num in range(3):
        ad = 0
        value = [0, 0, 0, 0, 0, 0]

        # record how many times in 0.05 seconds
        blank = [0, 0, 0, 0, 0, 0]
        count_times = [0, 0, 0, 0, 0, 0]
        for m in range(10):  # 5 times - 0.1 s
            # read data
            for i in range(6):
                aa = GPIO.input(self.IOlist[i])
                value[i] = aa

            for l in range(6):
                if value[l] == 1:
                    count_times[l] += 1

            time.sleep(0.02)

        # get real data
        for i in count_times:
            if i > 1:   # min count
                self.final_value = self.verify_data(value)
                self.final_value = self.check_data(self.final_value)

                return self.final_value

        return blank

    def verify_data(self, input_signal):
        count = 0
        blank = [0, 0, 0, 0, 0, 0]

        for i in input_signal:
            if i == 1:
                count += 1
        if count > 2:
            return blank
        else:
            return input_signal

    def check_data(self, input_signal):

        blank = [0, 0, 0, 0, 0, 0]

        # blank
        if input_signal == blank:
            self.count_data = blank
            return input_signal

        # count
        for i in range(6):
            if input_signal[i] == 1:
                self.count_data[i] += 1

        # verify
        for i in self.count_data:
            if i > self.max_count:
                return blank

        return input_signal


def test_touch():
    tc = Touch()
    while 1:
        print (tc.get_touch())
        time.sleep(0.1)
