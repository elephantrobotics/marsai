#!/usr/bin/env python
# encoding: utf-8

# Copyright (c) 2019 Elephant Robotics, Inc. All rights reserved.
# File name:    pythonapi.py
# Author:       Leonid, Joey
# Version:      1.01
# Date:         20, Jan, 2020
# Description:  python api to microcontroller
# Using this MarsAI source code is subject to the terms and conditions
# of Apache 2.0 License. Check LICENSE for more information

from ai import common
from ai import feature
from ai.feature import Feature
from touch import Touch
from distance import Distance

from datetime import datetime

import socket
import time
import random

import sys
sys.path.append(".")


class SensorFeatureGenerator:
    def __init__(self):
        self.tc = Touch()
        self.ds = Distance()

    def generate_sensor_feature(self):
        tc_ft = Feature()
        tc_ft.type = feature.Type.Touch.value
        tc_ft.received_time = int(
            (datetime.utcnow() - datetime(1970, 1, 1)).total_seconds() * 1000)
        tc_ft.timeout = int(random.uniform(100, 5000))
        tc_ft.data = self.tc.get_touch()

        ds_ft = Feature()
        ds_ft.type = feature.Type.TOFDistance.value
        ds_ft.received_time = int(
            (datetime.utcnow() - datetime(1970, 1, 1)).total_seconds() * 1000)
        ds_ft.timeout = int(random.uniform(100, 5000))
        ds_ft.data = self.ds.get_distance()

        return tc_ft, ds_ft

    def simulate_data_flow_forever(self):
        while True:
            while True:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.connect((common.HOST, common.PORT))
                    break
                except ConnectionRefusedError:
                    time.sleep(1)
                    continue

            tc_ft, ds_ft = self.generate_sensor_feature()

            sock.sendall(bytes(tc_ft.to_json() + "\n", "utf-8"))
            print("SEND: " + tc_ft.to_json())
            received = str(sock.recv(1024), "utf-8")
            #print("RECV: " + received)

            # time.sleep(0.2)
            sock.close()

            while True:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.connect((common.HOST, common.PORT))
                    break
                except ConnectionRefusedError:
                    time.sleep(1)
                    continue

            sock.sendall(bytes(ds_ft.to_json() + "\n", "utf-8"))
            print("SEND: " + ds_ft.to_json())
            received = str(sock.recv(1024), "utf-8")
            #print("RECV: " + received)

            sock.close()


if __name__ == "__main__":
    s = SensorFeatureGenerator()
    s.simulate_data_flow_forever()
