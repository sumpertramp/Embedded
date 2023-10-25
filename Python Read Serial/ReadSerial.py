from time import sleep
import sys
import time
import serial

readSerial = serial.Serial('COM5', baudrate = 115200, timeout = 1)

while 1:

    data = readSerial.readline()
    data = data.decode('utf-8')
    data = data.split(" ")

    if (len(data) > 0):
        print(data)

