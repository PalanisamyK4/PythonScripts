import math
a=math.radians(float(input("Enter the latitude of point 1: ")))
b=math.radians(float(input("Enter the longitude of that point: ")))
c=math.radians(float(input("Enter the latitude of point 2: ")))
d=math.radians(float(input("enter the longitude of that point: ")))
distance=6371.01*math.acos(math.sin(a)*math.sin(c)+math.cos(a)*math.cos(c)*math.cos(b-d))
print("The distance between the given 2 points is: ",distance)
