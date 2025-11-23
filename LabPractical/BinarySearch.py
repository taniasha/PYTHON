a = [10,20,30,50,60]
target = 50
low = 0
high = len(a)-1
while low <= high:
    mid = (low+high)//2
    if a[mid] < target:
        low = mid + 1
    elif a[mid] > target:
        high = mid - 1
    else:
        print("ELem found at index", mid)
        break
    
else:
    print("tHE ELEM IS not FOUND ")
        