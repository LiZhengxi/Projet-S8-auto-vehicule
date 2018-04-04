import serial
import time

ser = serial.Serial('/dev/ttyACM0',9600)
time.sleep(2)
while 1:
    str = raw_input("saisir : ");
    ser.write(str)