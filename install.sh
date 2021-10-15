#!/bin/bash

git clone git://github.com/bashwork/pymodbus.git
cd pymodbus
python setup.py install
chmod +x $PWD/powersupplycontrol/powersupplycontrol.py
cp $PWD/powersupplycontrol/powersupplycontrol.service /etc/systemd/system/
systemctl enable powersupplycontrol.service
systemctl start powersupplycontrol.service
