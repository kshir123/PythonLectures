# Class

class Calculator:
	def add(self, a, b):
		return a + b

calculator_obj = Calculator()

print(calculator_obj.add(2,3))

#____________________________________________________________________

# Object and Instance attribute

class Employee:
  company = 'Cybage'

omkar = Employee()
omkar.company = 'Google'
print(omkar.company)

#____________________________________________________________________

# Class attribute

class Employee:
  company = 'Cybage'

Employee.company  = 'Google'
print(Employee.company)

#__________________________________________________________________________

# self parameter

class Employee:
	def greet(self):
		print('Hello World !')

omkar = Employee()
omkar.greet()

#__________________________________________________________________________

# static method

class Employee:
  @staticmethod
  def greet():
    print('Hello World !')

omkar = Employee()
omkar.greet()

#________________________________________________________________________________

# __init__

class Employee:
  company = ''

  def __init__(self, company ):
    self.company = company

omkar = Employee('Cybage')
print(omkar.company)