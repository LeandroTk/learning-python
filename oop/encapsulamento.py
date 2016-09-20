# -*- coding: utf-8 -*-

class MyClass:
	prop1 = "I am a class property!"

	def __init__(self):
		print("The class {0} was iniciated").format(self.__class__)

	def _getProperty(self):
		return self.prop1

class MyOtherClass(MyClass):

	def setProperty(self, newval):
		self.prop1 = newval

Objeto1 = MyOtherClass()
print(Objeto1.getProperty)

# The class __main__.MyOtherClass was iniciated
# AttributeError: MyOtherClass instance has no attribute 'getProperty'

# ------------------------------------------------------------------------

class MyClass:
	prop1 = "I am a class property!"

	def __init__(self):
		print("The class {0} was iniciated").format(self.__class__)

	def _getProperty(self):
		return self.prop1

class MyOtherClass(MyClass):

	def setProperty(self, newval):
		self.prop1 = newval

	def callProtected(self):
		# chama o método getProperty
		return self._getProperty()

Objeto2 = MyOtherClass()
print(Objeto2.callProtected())

# The class __main__.MyOtherClass was iniciated
# I am a class property!