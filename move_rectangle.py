import distance
import copy
class Rectangle(object):
	"""Rectangle class. Its main attributes are a position (defined
	by a Point() object instance) width and height.
	"""

box = Rectangle()
box.width = 100
box.height = 200
box.corner = distance.Point()
box.corner.x = 0.0
box.corner.y = 0.0

def move_rectangle(rectangle, dx, dy):
	"""rectangle: Rectangle() object instance.
	dx, dy: numeric value
	Returns a copy of given rectangle, moved by dx and dy.
	"""
	new_rectangle = copy.deepcopy(rectangle)
	new_rectangle.corner.x += dx
	new_rectangle.corner.y += dy
	return new_rectangle


if __name__ == "__main__":
	rec = move_rectangle(box, 10, 10)
	print "Box position: ({x}, {y})".format(x=rec.corner.x,
											y=rec.corner.y)	