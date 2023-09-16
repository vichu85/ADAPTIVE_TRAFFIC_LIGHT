import serial
import time 
import math
arduino = serial.Serial(port='/dev/cu.usbmodem11201', baudrate=38400, timeout=.1) 

def write_read(x,sleep): 
	arduino.write(bytes(x, 'utf-8')) 
	time.sleep(0.05) 
	data = arduino.readline() 
	print("Sleeping")
	time.sleep(sleep)
	return data 

while True: 
	
	
	noOfCars = 14
	carTime = 5

	noOfTruck = 7
	truckTime = 10

	noOfLanes = 4
	greenTime = math.ceil(((noOfCars*carTime) + (noOfTruck * truckTime))/(noOfLanes+1))


	print(greenTime)
	
	value = write_read(str(1),greenTime) 
	value = write_read(str(2),greenTime) 
	value = write_read(str(3),greenTime)
	value = write_read(str(4),greenTime)
	print(value) 

