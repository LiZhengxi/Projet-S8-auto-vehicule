import serial

ser = serial.Serial('/dev/ttyACM0',9600)
s = [0,1]
while 1:
	read_serial=ser.readline()
	print read_serial
