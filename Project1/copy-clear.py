# Copy & Clear:
# Ek program likho jisme ek list banao, uska copy() banao aur fir clear() function ka use karke original list ko empty dikhayo.

mylist = [1,2,3,4,5]
newlist = mylist.copy()
print(newlist)

res = mylist.clear()
print(mylist)

print(newlist)