# Slection Sort work by putting largest eleemnt in front

a = [4, 1, 5, 2, 3]
n = len(a)
for i in range(n-1):
    minIndex = i
    for j in range(i+1, n):
      if(a[j] < a[minIndex]):
         minIndex = j    
   
    a[i], a[minIndex] = a[minIndex], a[i]

    print(f"After iteration {i+1}: {a}")
print(a)