a = [1,2,3,4,5]
s = 0 
e = 4
t = 1
while(s<=e):
 m = (s+e)//2   # ensures m is an integer
 if(t == a[m]):
  print("ELemnt found at :",m)
  break
 elif(t>a[m]):
   s= m+1
 else:
  e = m-1
else:
 print("Eleemnt not found")


#  m = s / 2 → float division
# Always returns a floating-point number, even if s is an integer.
# Example: 5 / 2 = 2.5

# m = s // 2 → integer (floor) division
# Returns the largest integer ≤ the result.
# Example: 5 // 2 = 2
