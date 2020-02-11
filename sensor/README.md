<!--
Copyright (c) 2019 Elephant Robotics, Inc. All rights reserved.

Using this MarsAI source code is subject to the terms and conditions of Apache 2.0 License. Check LICENSE for more information
-->

# Sensors

Sensors include distance sensor and touch sensor.
 * distance sensor : The distance can detect objects up to 3 meters.
 * touch sensors : The touch sensor includes 6 touch sensors: 3 in the head and 3 in the back.
 * gyro sensor: Gyro sensor commnication is embedded in API in library/pyfirmata.

## Setup SPI and I2C

Input `sudo raspi-config` in terminal to enable SPI and I2C communication for enable distance and touch sensors.