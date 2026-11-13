# String

a = 'Omkar'
b = "Omkar"
c = '''Omkar'''

#___________________________________________________________________________________

str = 'Omkar'

#   O  m  k  a  r
#   0  1  2  3  4   ← positive
#  -5 -4 -3 -2 -1   ← negative

print(str[0]) # O
print(str[-1]) # r

print(str[0: len(str)]) # Omkar

for i in str:  # O m k a r
    print(i)

#___________________________________________________________________________________

# Methods

print(len(str)) # Return the number of items in a container. : 5
print(str.find('r')) # Return the lowest index where substring is found. : 4
print(str.count('r')) # Return the number of occurrences of a substring. : 1
print(str.endswith('r')) # Return True if the string ends with the given suffix. : True
print(str.startswith('O')) # Return True if the string starts with the given prefix. : True
print(str.replace('r', 'n')) # Return a copy with all occurrences of old replaced by new. : Omkan
print(str.upper()) # Return a copy of the string converted to uppercase. : OMKAR
print(str.lower()) # Return a copy of the string converted to lowercase. : omkar

str = 'Python is an amazing language'
print(str.split(' ')) # Return a list of words using the given separator. : ['Python', 'is', 'an', 'amazing', 'language']

str = ' omkar '
print(str.strip()) # Return a copy with leading and trailing whitespace removed. : omkar

#___________________________________________________________________________________
