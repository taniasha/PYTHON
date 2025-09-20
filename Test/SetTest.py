# Question: Take two sets and perform:
# Union
# Intersection
# Difference
# Symmetric difference


set1 = {10, 20, 30, 40, 50}
set2 = {40, 50, 60, 70, 80}

print(set1.union(set2))

print(set1.intersection(set2))

print(set1.difference(set2))

print(set1.symmetric_difference(set2))

# ----------------------------------------------------------------------------------------------

# Question: Create a set and perform:
# Add an element (add)
# Add multiple elements (update)
# Remove an element (remove) and show difference with (discard)
# Clear the entire set (clear)

set3 = {1, 2, 3, 4, 5}

set3.add(6)
print(set3)

set3.update([6,7,8])
print(set3)

set3.remove(7)
print(set3)

set3.discard(0)
print(set3)

set3.clear()
print(set3)