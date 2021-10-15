#!/usr/bin/env python
# -*- coding: utf-8 -*-

# modbus_thread
# start a thread for polling a set of registers, display result on console
# exit with ctrl+c

import time
import os
import logging
from threading import Thread, Lock
from pyModbusTCP.client import ModbusClient

SERVER_HOST = "192.168.1.63"
SERVER_PORT = 502

# set global
regs = []
value = 1
timeout = False
# init a thread lock
regs_lock = Lock()

logging.basicConfig(	filename='/var/log/powersupply.log',
			filemode='a',
			format='[%(asctime)s] %(message)s',
			datefmt='%Y/%d/%m %H:%M:%S',
		    	level=logging.INFO)

# modbus polling thread
def polling_thread():
    global regs
    global value
    global timeout
    c = ModbusClient(host=SERVER_HOST, port=SERVER_PORT, timeout=5)
    logging.info('--------------')
    logging.info('Power Supply control started')
    # polling loop
    while True:
        # keep TCP open
        if not c.is_open():
           # print ("tcp not open")
	    c.open()
        else  :
          #  print("tcp open")
        # do modbus reading on socket
         reg_list = c.read_holding_registers(0)
        # if read is ok, store result in regs (with thread lock synchronization)
         if reg_list:
            with regs_lock:
                regs = list(reg_list)
		value = reg_list[0]
                timeout=False
         else :
             logging.info("Modbus TCP Timeout")
             timeout=True
    # 1s before next polling
        time.sleep(1)


# start polling thread
tp = Thread(target=polling_thread)
# set daemon: polling thread will exit if main thread exit
tp.daemon = True
tp.start()

# display loop (in main thread)
while True:
    # print regs list (with thread lock synchronization)
 if not timeout :
    with regs_lock:
        if value==1:
		logging.info("power supply ok")
	else: 
		logging.info("power supply off, shutting down")
                os.system("shutdown -h now")
    #	print(value)
    # 1s before next print
    time.sleep(1)
logging.info('Power Supply control ended')
