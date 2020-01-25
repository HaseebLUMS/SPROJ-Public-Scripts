class Class0():
	def func1(self):
		print("Class0")
class Class1():
	def func1(self):
		print("Class1")
class ClassA(Class1, Class0):
	def funcA(self):
		print("ClassA")
	def func1(self):
		print("ClassA")
a = ClassA()
a.func1()