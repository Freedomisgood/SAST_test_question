from data import path_name
from datetime import datetime
from functools import wraps
import os 
def add_log(func):
	@wraps(func)
	def inner():
		try:
			with open (path_name,'a') as f:
				pass
		except FileNotFoundError:
			os.makedirs(os.path.split(path_name)[0])
			with open (path_name,'a') as f:
				f.write(str(datetime.now()) +'-----' + os.path.realpath(__file__) +'-----'+ test.__name__+"\n")
		else:
			func()
	return inner

@add_log
def test():
		with open (path_name,'a') as f:
			f.write(str(datetime.now()) + '-----' +os.path.realpath(__file__) +'-----'+ test.__name__ + "\n")
test()
