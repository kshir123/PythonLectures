# range() generates a sequence of numbers. Think of it as saying 
# "count from here to there"

# range(stop)               # 0 up to stop-1
# range(start, stop)        # start up to stop-1
# range(start, stop, step)  # start, jumping by step

list(range(5))         # [0, 1, 2, 3, 4]
list(range(1,6))       # [1, 2, 3, 4, 5]
list(range(0,10,2))    # [0, 2, 4, 6, 8]

for i in range(1, 6):
    print(i) # 1  2  3  4  5

#___________________________________________________________________________

# Strings

name = 'Omkar'

for i in name:
    print(i) # o m k a r

#___________________________________________________________________________

# List 

ls = [1, 2, 3, 4, 5, 6]

for i in ls:
    print(i) # 1 2 3 4 5 6

#___________________________________________________________________________

# For loop with Dict

dict = {
   'name' : 'Omkar',
   'age' : 28
}

for i in dict:
   print(dict[i])
