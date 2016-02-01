from swampy.TurtleWorld import *

world =  TurtleWorld()
bob = Turtle()
bob.delay = 0.001

def make_koch(t, length):
	if(length < 3):
		fd(t, length)
	else:
		m = (length / 3.0)
		make_koch(t, m)
		lt(t, 60)
		make_koch(t, m)
		rt(t, 120)
		make_koch(t, m)
		lt(t, 60)
		make_koch(t, m)

def snowflake(t, n):
	for i in range(3):
		make_koch(t, n)
		rt(t, 120)



snowflake(bob, 100)

wait_for_user()