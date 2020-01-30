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
`sudo systemctl enable [any service]`

## Disable
Disable the service and the service will not run when next boot.
`sudo systemctl disable [any service]`

## Start
Start the service.
`sudo systemctl start [any service]`

## Stop / Pause and Shutdown
Stop the existing service.
`sudo systemctl stop [any service]`