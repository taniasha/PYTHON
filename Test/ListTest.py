# 1. Question: Create a list and perform the following operations:
# Add an element (append)
# Insert an element at a specific position (insert)
# Remove an element (remove)
# Reverse the list (reverse)
# Sort the list (sort)

list1 = [11,12,13,15,14]
list1.append(16)
print(list1)

list1.insert(0,10)
print(list1)

list1.remove(13)
print(list1)

list1.reverse()
print(list1)

list1.sort()
print(list1)

# -------------------------------------------------------------------------------------------------

# 2. Question: Take a list and do the following:
# Find maximum, minimum, and sum (max, min, sum)
# Find the frequency of an element (count)
# Find the index of an element (index)

list2 = [10,20,30,40,50]

print(max(list2))
print(min(list2))
print(sum(list2))
print(list2.count(10))
print(list2.index(30))