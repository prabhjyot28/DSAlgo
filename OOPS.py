#Why do we need classes?

# Classes are templates and if we make the instance of that template it's known as Object.



# instance variables are those data which are unique to each instances/objects.
# class variables are common for each intances of the class and shared among each of the
# class.

# class variables can be called through name of class as well as class instance.


# if we change the class variable by calling it through one of its instance, then it'll
# actually create a new property for that instance intead of actually changing the class 
# variable.



# Similar to class variables we also have class methods, which is common for all the 
# the instances of the class, 
# classmethod automatically pass class as the first argument.




# classmethod can be used as an alternative constructor.

@classmethod
def from_string(cls, emp_str):
	first, last, pay = emp_str.split('-')
	return cls(first, last, pay)


# staticmethod neither operates on the instance or the class.

@staticmethod
def isWorkDay(day):
	if day.weekday() == 5 or day.weekday()==6:
		return False
	return True


# abstarctmethod are those that dont have any implementation yet.
# abstarctclass are those which contains abstarctmethods, and they cant be instantiated.
# abstarction in python is achieved using abc module.

from abc import ABC, abstractmethod


class Myclass(ABC):
	@abstractmethod
	def somemethod(self):
		pass


# Myclass can't be instantiated because it's a abstract class.







#  INHERITANCE



class Developer(Employee):
	
	def __init__(self, a, b, c):
		super().__init__(a, b)
		self.c = c



# isinstance(emp, Employee)     =>   checks whether emp is instance of Employee.
# issubclass(Manager, Employee)  => checks whether Manager is sunbclass of Employee.









# Special class methods / dunder methods / Magic methods

# __init__     =>  to instatnciate a class.
# __repr__     => to print an instance of class, (when __str__ is absent).
# __str__      => to represent an instance of class.
# __add__, __sub__, __mul__, __and__, __or__, __pow__, __len__




# Operators overloading is performed using this dunder methods.


# Example if we want to customize the behaviour of + sign.

def __add__(self, other):
	return self.pay+other.pay

print(emp1 + emp2)










# @property  => is used to access the property using a function.
# @property.setter  => is set a property and other according to it.
# @property.deleter  =>  is set to delete a property and change others accordingly.




class Employee:

	def __init__(self, first, last):
		self.first = first
		self.last = last

	@property
	def fullname(self):
		return self.first + ' ' + self.last


	@fullname.setter
	def fullname(self, name):
		first, last = name.split(' ')
		self.first = first
		self.last = last

	@fullname.deleter
	def fullname(self):
		print('Deleting name !')
		self.first = None
		self.last = None






#--------------------------POLYMORPHISM------------------#
# It means having many forms.
# In programming terms, it means same function name (different arguments) being used for 
# different types.
 


# In Python, Polymorphism lets us define methods in the child class that have the same
# name as the methods in the parent class. In inheritance, the child class inherits the
# methods from the parent class. However, it is possible to modify a method in a child
# class that it has inherited from the parent class. This is particularly useful in cases
# where the method inherited from the parent class doesn’t quite fit the child class. 
# In such cases, we re-implement the method in the child class. This process of 
# re-implementing a method in the child class is known as Method Overriding.













