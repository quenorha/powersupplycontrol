#!/bin/bash

apt-get update
apt-get -y install python-pip
pip install pyModbusTCP
chmod +x /root/powersupplycontrol/powersupplycontrol.py
cp /root/powersupplycontrol/powersupplycontrol.service /etc/systemd/system/
systemctl enable powersupplycontrol.service
systemctl start powersupplycontrol.service
