# Question: Create a tuple and perform:
# Count occurrences of an element (count)
# Find the index of an element (index)

tuple1 = (10, 20, 30, 40, 50, 30)
print(tuple1.count(30))

print(tuple1.index(30))

# ----------------------------------------------------------------------------------------------

# Convert it into a list (list())
# Convert it back into a tuple (tuple())
# Use slicing to extract middle elements

print(list(tuple1))

print(tuple(tuple1))

# print(tuple1(slice(2,4))) --- give error
print(tuple1[slice(2,5)])