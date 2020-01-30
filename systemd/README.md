<!--
Copyright (c) 2019 Elephant Robotics, Inc. All rights reserved.

Using this MarsAI source code is subject to the terms and conditions of Apache 2.0 License. Check LICENSE for more information
-->

# Systemmd

This is used to auto-start all the services when boost the Raspberry PI. You can enable, disable, start or stop four different service by using following code:

## Service
 * mars-main
 * mars-vision
 * mars-voice
 * mars-sensors

## Enable
Enable the service and the service will auto-run when next boot.
example: `sudo systemctl enable mars-main ` 

## Disable
Disable the service and the service will not run when next boot.
example: `sudo systemctl disable mars-main `

## Start
Start the service.
example: `sudo systemctl start mars-main `

## Stop / Pause and Shutdown
Stop the existing service.
example: `sudo systemctl stop mars-main `