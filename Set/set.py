# remove duplicates
myset = {1,2,3,4,4}
print(myset) 

set1 = {1,2,3,4}
set2 = {3,4,5,6}

set1.add(5)
print(set1)

set1.remove(1) # remove element (error if not found)
print(set1)

set1.discard(2) # remove if exists, else ignore
print(set1)


res = set1 | set2  #union
print(res)

print(set1 & set2) #intersection
print(set1.intersection(set2))

print(set1 - set2)
print(set1.difference(set2))


print(set1)
print(set2)
print(set1.issubset(set2))
print(set2.issubset(set1))

print(set1.issuperset(set2))
print(set2.issuperset(set2))