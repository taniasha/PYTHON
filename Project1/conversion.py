# Ek program likho jisme ek list ko tuple me aur ek tuple ko list me convert karke usme elements 
# add/remove karke print karo.

# list to tuple
list1 = [1,2,3,4]
print("List to tuple: ", tuple(list1))

list1.append(7)
print("After adding elem : ", tuple(list1))

# ---------------------------------------------------------------------------------------


# tuple to list
tuple1 = (2,4,6,8)
t = list(tuple1)
print("Tuple to List : ", t)

t.remove(4)
print("remove elem: ", t)

