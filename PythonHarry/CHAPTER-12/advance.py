# The Walrus operator

num = [1,2,3,4,5]

if (n := len(num)) > 3:
  print(f'List is long : {n} items')

#___________________________________________________________________________________

# Type definitions

age: int = 20

def greet() -> str:
  return 'Hi'

print(greet())

numbers: list[int] = [1,2,3,4]
dict : dict[str, int] = { 'name' : 'Omkar', 'age': 28}

#___________________________________________________________________________________________

# Match case

def http_status(code):
  match code:
    case 200:
      return 'OK'
    case 404 :
      return 'NOT FOUND'
    case 500 | 502:
      return 'SERVER ERROR'
    case _:
      return 'UNKNOWN'
  
print(http_status(404))
print(http_status(502))
print(http_status(999))

#__________________________________________________________________________________________

# if __name__ == '__main__': 

def main(): 
  print("App started") 

if __name__ == '__main__': 
  main() 

#__________________________________________________________________________________

# enumerate()

fruits = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruits):
  print(i, fruit)

#___________________________________________________________________________________

# List comprehension

nums = [1,2,3,4]

squares = [n*n for n in nums]

print(squares)

#_______________________________________________________________________________

# Lambda Function

add = lambda a, b: a + b

print(add(2, 3))   # 5

#__________________________________________________________________________________

# Map , filter, reduce

from functools import reduce   # reduce must be imported

nums = [1, 2, 3, 4, 5]

# map: transform every item
print(list(map(lambda n: n * 2, nums)))          # [2, 4, 6, 8, 10]

# filter: keep items that pass a test
print(list(filter(lambda n: n % 2 == 0, nums)))  # [2, 4]

# reduce: combine all items into one value
print(reduce(lambda a, b: a + b, nums))          # 15

#__________________________________________________________________________________________
