class Parent(object):
	"""docstring for parent"""
	def overide(self):
		print("PARENT overide()")

	def implicit(self):
		print("PARENT implicit()")

	def altered(self):
		print("PARENT altered()")

class Child(Parent):
	"""docstring for subclass child """
	def overide(self):
		print("CHILD overide()")

	def altered(self):
		print("CHILD, BEFORE PARENT altered()")
		super(Child, self).altered()#super calls function on parent class from named subclass
		print("CHILD,AFTER PARENT altered()")
	
	"""is a relationship """
dad = Parent()
son = Child()

dad.implict()
son.implicit()
""" has a relationship """
dad.altered()
son.altered()
		

