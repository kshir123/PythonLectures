dict = {
    'name' : 'Omkar',
    'age' : 28
}

# Read
print(dict['name'])         # Omkar
# Update
dict['age'] = 20
# Add
dict['course'] = 'Python'
# Delete
del dict['name']

# Iterate
for i in dict:              # 20
    print(dict[i])          # Python

for key, value in dict.items():     # age-20
    print(f'{key}-{value}')         # course-Python

# Methods
print(dict.keys())          # dict_keys(['age', 'course'])
print(dict.values())        # dict_values([20, 'Python'])
print(dict.items())         # dict_items([('age', 20), ('course', 'Python')])
print(dict.update({'course': 'python'}))    # None
print(dict.pop('age'))      # 20
print(dict.popitem())       # ('course', 'python')
print(dict.clear())         # None


# Merging dict
# merged = dict1 | dict2