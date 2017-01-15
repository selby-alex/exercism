
class Clock:
	def __init__(self, hour, minute):
		self.h = hour
		self.m = minute
		self.timeset()

	def timeset(self):
		ms = (self.m + (self.h * 60))
		self.h = (ms / 60) % 24
		self.m = ms % 60

	def add(self, minute):
		self.m += minute
		self.timeset()
		return self

	def __eq__(self, other):
		return self.__dict__ == other.__dict__

	def __str__(self):
		return "%s:%s" % (str(self.h).zfill(2),str(self.m).zfill(2))


#print(Clock(15,37),Clock(15,37))
##self.assertEqual('08:00', str(Clock(8, 0)))
##self.assertEqual('04:43', str(Clock(0, 1723)))
#x = Clock(5,-1490)
#y = Clock(4,10)

#print x,y