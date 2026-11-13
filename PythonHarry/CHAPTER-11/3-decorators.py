# Super
class Parent:
  def parent_skill(self):
    print('Walking')

class Child(Parent):
  def child_skill(self):
    super().parent_skill()         
    print('Talking')

c = Child()

c.child_skill()

#______________________________________________________________________

# @classmethod

class Employee:
    company = 'Cybage'              

    @classmethod
    def show_company(cls):          
        print(cls.company)

Employee.show_company()              # Cybage
omkar = Employee()
omkar.show_company()                 # Cybage

#____________________________________________________________________

# @property decorators

class Employee:
  def __init__(self, company):
    self.__company = company

  @property
  def company(self):
    return self.__company

omkar = Employee('Cybage')
print(omkar.company)   # Cybage (no brackets)

#____________________________________________________________________

# Getter and Setter

class Employee:
  def __init__(self, company):
    self.__company = company
  
  @property
  def company(self):
    return self.__company

  @company.setter
  def company(self, company):
    if company:
      self.__company = company

omkar = Employee('Cybage')
print(omkar.company)

#____________________________________________________________________

# Operator overloading

class Employee:
  def __init__(self, salary):
    self.salary = salary
  
  def __add__(self, other):
    return self.salary + other.salary

e1 = Employee(2)
e2 = Employee(2)

print(e1 + e2)
