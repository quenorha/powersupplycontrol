#!/bin/bash

git clone https://github.com/sourceperl/pyModbusTCP.git
cd pyModbusTCP
sudo python setup.py install
pip install pyModbusTCP
chmod +x /root/powersupplycontrol/powersupplycontrol.py
cp /root/powersupplycontrol/powersupplycontrol.service /etc/systemd/system/
systemctl enable powersupplycontrol.service
systemctl start powersupplycontrol.service
