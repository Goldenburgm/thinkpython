from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

def draw(t, length, n):
	if n == 0:
		return
	angle = 50
	fd(t, length * n)
	lt(t, angle)
	draw(t, length, n-1)
	rt(t, 2 * angle)
	draw(t, length, n-1)		
	lt(t, angle)
	bk(t, length * n)

draw(bob, 0.5, 30)