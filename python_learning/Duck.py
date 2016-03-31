class Duck():
	def __init__(self, name):
		self.__private_name = name
	@property
	def name(self):
		return self.__private_name
	@name.setter				
	def name(self, input_name):
		self.__private_name = input_name
