class Parent():
	def __init__(self,last_name,eye_color):
		print("Parent constructor called")
		self.last_name=last_name
		self.eye_color=eye_color	




class Child(Parent):
	"""docstring for ClassName"""
	def __init__(self,last_name,eye_color,number_of_toys):
		print("child constructor called")
		Parent.__init__(self,last_name,eye_color)
		self.number_of_toys = number_of_toys

		

kela=Child("Bhai","Blue",5)
print(kela.number_of_toys)
print(kela.last_name)		