import math
from mypolygon import *

def draw_pie(t, n, r):
	"""Draws a pie, then moves into a position to the right.

	t: Turtle
	n: number of segments
	r: length of the radial spokes
	"""
	polypie(t, n, r)
	pu(t)
	fd(t, r * 2 + 10)
	pd(t)

def polypie(t, n, r):
	"""Draws a pie divided into radial segments.

	t: Turtle
	n: number of segments
	r: length of the radial spokes
	"""

	angle = 360.0 / n
	for i in range(n):
		isosceles(t, r, angle / 2)
		lt(t, angle)

def isosceles(t, r, angle):
	"""Draws an isosceles triangle.

	The turtle starts and ends at the peak, facing the midle of the base.

	t: Turtle
	r: length of the equal legs
	angle: peak angle in degrees
	"""

	y = r * math.sin(angle * math.pi / 180)

	rt(t, angle)
	fd(t, r)
	lt(t, 90 + angle)
	fd(t, 2 * y)
	lt(t, 90 + angle)
	fd(t, r)
	lt(t, 180 - angle)

draw_pie(bob, 10, 30)
wait_for_user()