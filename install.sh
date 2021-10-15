#!/bin/bash

apt-get install pip
pip install pymodbus
chmod +x /root/powersupplycontrol/powersupplycontrol.py
cp /root/powersupplycontrol/powersupplycontrol.service /etc/systemd/system/
systemctl enable powersupplycontrol.service
systemctl start powersupplycontrol.service
