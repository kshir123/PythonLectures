# list
ls = ['Omkar', 23, 3.0, True, None]

print(ls[0]) # Omkar
print(ls[-1]) # None

print(ls[0:len(ls)]) # ['Omkar', 23, 3.0, True, None]

ls[0] = 'Salt' 

for i in ls: # 'Omkar'  23  3.0  True  None
    print(i)

#___________________________________________________________________________________

ls = [1,2,3,4,5]

print(len(ls)) # 5
ls.append(6) # Append object to the end of the list. : None
ls.insert(6, 7) # Insert object before index.: None
ls.remove(1) # Remove first occurrence of value. Raises ValueError if the value is not present. : None
print(ls.pop()) # Remove and return item at index (default last). Raises IndexError if list is empty or index is out of range. : Value
ls.sort() # Sort the list in ascending order and return  : None.
ls.reverse() # reverse the list : None
ls.clear() # Remove all items from the list : None

#___________________________________________________________________________________

days = ('MONDAY', 'TUESDAY', 'WEDNESDAY', 'THRUSDAY')

print(days[0])
# days[0] = 'X' # ❌ 'tuple' object does not support item assignment

print(days.index('MONDAY')) # 0
print(days.count('MONDAY')) # 1

#___________________________________________________________________________________
