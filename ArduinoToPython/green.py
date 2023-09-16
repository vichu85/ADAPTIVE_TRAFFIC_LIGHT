import math

noOfCars = 14
carTime = 10

noOfTruck = 7
truckTime = 30

noOfLanes = 4
greenTime = math.ceil(((noOfCars*carTime) + (noOfTruck * truckTime))/(noOfLanes+1))


print(greenTime)