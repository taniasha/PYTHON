a = [19, 20, 1, 4, 2]

n = len(a)

for i in range(n-1):
    minIndex = i
    for j in range(i+1, n):
        if a[j] < a[minIndex]:
            minIndex = j

        min_value = a.pop(minIndex)
        a.insert(i, min_value)

    print(a)