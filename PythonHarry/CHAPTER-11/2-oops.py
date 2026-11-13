# Encapsulation 
class Employee:
    def __init__(self, company):
        self.__company = company   # hidden

    def get_company(self):
        return self.__company

omkar = Employee('Cybage')
print(omkar.get_company())   # Cybage
# print(omkar.__company)     # error

'''
__company is locked. Use get_company() to read it.

Python’s naming conventions:
company: public, anyone can use it
_company: “protected” by convention, meaning “please don’t touch” (nothing stops you)
__company: private-ish, name gets mangled to _Employee__company
'''
#__________________________________________________________________________________________________

# Abstraction

class Employee:
  def __init__(self, company):
    self.__company = company   # hidden

  def get_company(self):
    return self.__company

omkar = Employee('Cybage')
rahul = Employee('TCS')

# Each Employee object keeps its own hidden company, and you read it with get_company().

#_____________________________________________________________________________________________________

# Inheritance

class Parent: 
  def parent_skill(self):
    print('walking')

class child(Parent):
  def child_skill(self):
    print('Talking')

c = child()

c.parent_skill()
c.child_skill()

# Multiple Inheritance

class Father:
  def father_skill(self):
    print('Walking')

class Mother:
  def mother_skill(self):
    print('Talking')

class child(Father, Mother):
  def child_skill(self):
   print('Dancing')

c = child()

c.father_skill()
c.mother_skill()
c.child_skill()

# Multilevel Inheritance

class Grandparent:
  def grand_parent(self):
    print('Walking')

class Parent(Grandparent):
  def parent_skill(self):
    print('Talking')

class Child(Parent):
  def child_skill(self):
    print('Dancing')


c = Child()

c.grand_parent()
c.parent_skill()
c.child_skill()

#_______________________________________________________________________________

# Polymorphism

class Employee:
  def work(self):
    print('Working')

class Developer(Employee):
  def work(self):              # overrides parent
    print('Writing code')

Employee().work()    # Working
Developer().work()   # Writing code