from collections import deque

class RunningError(Exception): 
	pass

class PowerError(Exception):
	pass

def RunningError():
	pass

def PowerError():
	pass

class Sensor ():
	def __init__(self):
		self._power = False
		self._running = True
	
	@property
	def power(self):
		return self._power
	
	@property
	def running(self):
		return self._running

	@power.setter
	def power(self,value):
		_power = value
		
	@running.setter
	def running(self,value):
		if value == True:
			if self._power == False:
				try:
					PowerError()
				except PowerError:
					self._running = True
			else:
				_running = value
		else:
			_running = value

class TemperatureSensor(Sensor):
	def __init__(self,_power,_running):
		super().__init__(self,times)
		y=deque([],times)

	def add_data(self,value):
		if self._running == False:
			if self._power == False:
				try:
					PowerError()
				except PowerError:
					print ('PowerError')
			else:	
				try:
					RunningError()
				except RunningError:
					print ('RunningError')
		else:
			y.append(value)

	def get_data(self):
		if self._running == False:
			if self._power == False:
				try:
					PowerError()
				except PowerError:
					print ('PowerError')
			else:	
				try:
					RunningError()
				except RunningError:
					print ('RunningError')
		else:
			return sum(y)/len(y)