
import os
file_path = os.path.join(os.path.dirname(__file__), 'demo.txt')

# Read whole file
with open(file_path, 'r') as f:
    print(f.read())

# Write (Overwrite file)
with open(file_path, 'w') as f:
    f.write("Hello World")

# Read all lines into list
with open(file_path) as f:
    lines = f.readlines()
    print(lines)

# Read one line at time
with open(file_path) as f:
    for line in f:
        print(line.strip())
        
# Context Managers
# with (open(file_path1) as f1, open(file_path2) as f2):
#   print(f1.read())
#   print(f2.read())