class Point:
	def __init__(self, x = 3, y =4):
		self.move(x, y)
		
	def move(self, x, y):
		self.x = x
		self.y = y
		
	def reset(self):
		self.move(0, 0)
