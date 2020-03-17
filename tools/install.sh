#!/bin/bash

sudo cp systemd/mars-*.service /etc/systemd/system/

for service in $(cd /etc/systemd/system/; ls mars-*.service); do
	sudo systemctl enable $service
	sudo systemctl restart $service
done
