<!--
Copyright (c) 2019 Elephant Robotics, Inc. All rights reserved.

Using this MarsAI source code is subject to the terms and conditions of Apache 2.0 License. Check LICENSE for more information
-->

# Pyfirmata

Pyfirmata is the API for controlling micro-controller of all 16 servos and gyro sensor. You can use it to commnicate with each servo motor and control MarsCat move, run and turn.

## API
 * `setTailAngle(servo_no, angle, speed)` : `servo_no`: 1 or 2; `speed`: 0.0 ~ 1.0;
 * `setHeadAngle(servo_no, angle, speed)` : `speed`: 0.0 ~ 1.0;
 * `setLegAngle(leg_no, servo_no, angle, speed)` :  `leg_no`: 1 ~ 4; `servo_no`: 1 ~ 3; `speed`: 0.0 ~ 1.0;
 * `getLegAngle(leg_no, servo_no)` : `leg_no`: 1 ~ 4; `servo_no`: 1 ~ 3
 * `setLegCoordOffset(leg_no, dx, dy, dz, speed)` : `speed`: 0.0 ~ 1.0;
 * `getGyroData(is_rx)` :
 * `setIniGait(mode, speed)` :
 * `setCOGOffset(dx, dy, dz, drx, dry, drz, speed)` :
 * `setBalance()` :
 * `setRun(speed)` : `speed`: 0.0 ~ 1.0;
 * `setTurn(direction, speed)` : `speed`: 0.0 ~ 1.0;
 * `setWalk(speed)` : `speed`: 0.0 ~ 1.0;
 * `setStop()` :

## Examples

Check example file to test the commnucation between python to micro-controller.
 * important: the MarsCat is needed to test.