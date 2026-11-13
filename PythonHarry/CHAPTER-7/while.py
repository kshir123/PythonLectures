# While
i = 0

while i < 5 :
    print(i) # 0 1 2 3 4 
    i += 1
# _______________________________________________________________________

# String

name = 'omkar'

i = 0

while i < len(name):
    print(name[i]) # o m k a r
    i += 1

#________________________________________________________________________

# list

ls = [1, 2, 3, 4, 5]

i = 0

while i < len(ls): 
    print(ls[i]) # 1 2 3 4 5
    i += 1

#________________________________________________________________________

# Dict

dict = {
    'name' : 'Omkar',
    'age' : 28
}

keys = list(dict.keys())
i = 0

while i < len(dict):            
    key = keys[i]
    print(f'{key} : {dict[key]}')   # name : Omkar 
    i += 1                          # age : 28
