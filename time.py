import datetime

class Time(object):
	"""Represents time in hours, minutes and seconds.
	"""

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
	new_time = int_to_time((time_to_int(t) + seconds))
	return new_time

def time_to_int(t):
	"""t: Time() object.
	Converts given time attributes to a single integer value.
	"""	
	minutes = t.hour * 60 + t.minute
	seconds = minutes * 60 + t.second
	return seconds

def int_to_time(n):
	"""n: integer
	Converts given integer to a Time() object.
	"""	
	time = Time()
	minutes, time.second = divmod(n, 60)
	time.hour, time.minute = divmod(minutes, 60)
	return time

def add_time(t1, t2):
	"""t1, t2: Time() objects.
	Returns a new Time() that is the sum of both time objects.
	"""	
	res = time_to_int(t1) + time_to_int(t2)
	return int_to_time(res)

def mul_time(t1, n):
	"""t1: Time() object.
	n: numeric value.
	Returns a new Time() that is the product of t1 times n.
	"""
	res = time_to_int(t1) * n
	return int_to_time(res)

def average_pace(t, distance):
	"""t: Time() object.
	distance: distance in miles.
	Considering it took t to go over given distance, returns the
	average pace in miles per second.
	"""	
	res = float(distance) / float(time_to_int(t))
	return res

def week_day():
	"""
	Prints the day of the week.
	"""
	current_time = datetime.datetime.now()
	week_days = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday",
				 4:"Friday", 5:"Saturday", 6:"Sunday"}
	week_day = current_time.weekday()
	print "Today is {}".format(week_days[week_day])



if __name__ == "__main__":
	time = Time()
	time.hour = 0
	time.minute = 0
	time.second = 30

	time2 = Time()
	time2.hour = 21
	time2.minute = 2
	time2.second = 34
	
	week_day()
	