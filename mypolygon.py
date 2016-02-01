#imports
from swampy.TurtleWorld import * 
import math 
 
#instancing turtles and turtle worlds, and adjusting Bob's delay as well
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01


def square(t):
	"""Square takes a turtle and draws a simple 100x100 square"""
	for i in range(4):
		fd(t, 100)
		lt(t)

def square2(t, length):
	"""Square 2 takes a turtle and a length, and draws a length x length square"""
	for i in range(4):
		fd(t, length)
		lt(t)

def polygon(t, n, length):
	"""Polygon takes a turtle, a number of sides (n) and a length, and 
	draws an n sided polygon"""
	angle = 360.0 / n
	for i in range(n):
		fd(t, length)
		lt(t, angle)

def circle(t, r):
	"""Circle takes a turtle and a radius. With given radius, 
	it finds out the circumference and draws a circle using
	polygon"""
	circumference = 2 * math.pi * r
 	n = int(circumference / 3) + 1
 	length = circumference / n
 	polygon(t, n, length)

def polyline(t, n, length, angle):
	"""A generalized version of polygon"""
	for i in range(n):
		fd(t, length)
		lt(t, angle)

def arc(t, r, angle):
	"""Draws an arc according to given radius and angle. Ex: if given 360, arc draws 
	a complete circle"""
	arc_length = 2 * math.pi * r * angle / 360
	n = int(arc_length / 3) + 1
	step_length = arc_length / n
	step_angle = float(angle) / n 

	polyline(t, n, step_length, step_angle)



