import math

def eval_loop():
	while True:
		if command != "done":
			command = raw_input("")
			print ">",
			print eval(str(command))
			last_command = command
		else: 
			print ">",
			print eval(str(last_command))
			break	


		
 	
		


eval_loop()		




			