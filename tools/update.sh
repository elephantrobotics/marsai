#!/bin/bash
if [ ps -C update.sh ]; then
	# Already running in another tty
	exit
fi
usb_disks=$(mount | grep '/media/pi/' | cut -d' ' -f3)
for usb_disk in $usb_disks; do
	if [ -e $usb_disk/MarsApp.zip ]; then
		# Stop running apps
		# Replace MarsAI
		if [ -e marsai.bak ]; then
			rm -rf marsai.bak
		fi
		mv marsai marsai.bak
		unzip $usb_disk/MarsApp.zip
		# Remove old services
		mkdir systemd.bak
		sudo mv /etc/systemd/system/mars-*.service systemd.bak/
		# Replace services
		sudo cp systemd/mars-*.service /etc/systemd/system/
		# Copy previous personality files (if new ones do not exist)
		# Restart services
		for service in $(cd /etc/systemd/system/; ls mars-*.service); do
			sudo systemctl restart $service
		done
		# Restart apps (if they were running)
		# Log
		echo -n 'Updated ' >> ~/update.out
		date >> ~/update.out
		# Break out of loop (don't try other USBs)
		break
	fi
done
