from swampy.TurtleWorld import *
from mypolygon import *
import math

def petal(t, r, angle):
	"""Draws a petal using two arcs.
	t: Turtle
	r: radius of the arcs
	angle: angle (degrees) that subtends the arcs
	"""
	for i in range(2):
		arc(t, r, angle)
		lt(t, 180 - angle)

def flower(t, n, r, angle):
	"""Draws a flower with n petals.

	t: Turtle
	r:  radius of the arcs
	angle: angle (degrees) that subtends the arcs
	"""

	for i in range(n):
		petal(t, r, angle)
		lt(t, 360.0/n)

def move(t, length):
	"""Move turtle (t) forward (length) units without leaving a trail
	Leaves the pen down.
	"""
	pu(t)
	fd(t, length)
	pd(t)


flower(bob, 10, 60, 80)
wait_for_user()