class Time(object):
	"""Represents time in hours, minutes and seconds.
	"""

time = Time()
time.hour = 21
time.minute = 1
time.second = 50

time2 = Time()
time2.hour = 21
time2.minute = 2
time2.second = 34

def print_time(t):
	"""Receives: Time() object.
	Prints given time in hour:minute:second format.
	"""	
	print "{:02d}:{:02d}:{:02d}".format(t.hour, t.minute, t.second)

def is_after(t1, t2):
	"""t1, t2: Time() objects.
	Tests if t1 comes after t2 chronologically, returning false if it 
	doesn't.
	"""	
	t1_tuple = (t1.hour, t1.minute, t1.second)
	t2_tuple = (t2.hour, t2.minute, t2.second)
	return t1_tuple > t2_tuple

def increment_seconds(t, seconds):
	"""t: Time() object
	seconds: integer
	Returns new Time() object with added seconds.
	"""	
	new_time = Time()
	new_time.hour = t.hour
	new_time.minute = t.minute
	new_time.second = t.second

	new_time.second += seconds

	if new_time.second >= 60:
		remainder = new_time.second % 60
		new_time.minute += seconds / 60
		new_time.second = remainder

	if new_time.minute >= 60:
		remainder = new_time.minute % 60
		new_time.hour += new_time.minute / 60
		new_time.minute = remainder

	return new_time		

if __name__ == "__main__":
	new_time = increment_seconds(time, 4000)
	print_time(time)
	print_time(new_time)