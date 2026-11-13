s = {1, 2, 2, 3, 3, 3}
print(s)   # {1, 2, 3} — duplicates removed!

#__________________________________________________________________________________

# Methods
s = {1, 8, 2, 3}

print("Length of  set:", len(s)) # Length of set: 4

s.add(54)
print("After ad ding 54:", s) # After adding 54: {1, 2, 3, 8, 54} (unordered)

s.remove(8)
print("After removing 8:", s) # After removing 8: {1, 2, 3, 54}

s.discard(99) # Does nothing, no error

popped_val = s.pop()
print(f"Popped value: {popped_val}, Remaining set: {s}") # Popped value: 1, Remaining set: {2, 3, 54}

s.clear()
print("After clear():", s) # After clear(): set()

#__________________________________________________________________________________

# Set Operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b   # Union         → {1,2,3,4,5,6}
a & b   # Intersection  → {3,4}
a - b   # Difference    → {1,2}
a ^ b   # Symmetric diff→ {1,2,5,6}

# Union
print("Union:", a.union(b)) # Union: {1, 2, 3, 4, 5, 6}
print("Intersection:", a.intersection(b)) # Intersection: {3, 4}
print("Difference (s1 - s2):", a.difference(b)) # Difference (s1 - s2): {1, 2}
print("Symmetric Difference:", a.symmetric_difference(b)) # Symmetric Difference: {1, 2, 5, 6}
