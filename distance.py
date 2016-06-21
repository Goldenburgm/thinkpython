import math

class Point(object):
	"""Represents a point in 2D space.
	"""

p1 = Point()
p2 = Point()

p1.x = -2
p1.y = 1
p2.x = 1
p2.y = 5

def calc_distance(p1, p2):
	"""p1, p2: Point() object instances.
	Calculates the distance between two given points.
	"""
	distance = math.sqrt(math.pow((p2.x-p1.x), 2)+  
						 math.pow((p2.y-p1.y), 2))
	return distance

print calc_distance(p1, p2)	