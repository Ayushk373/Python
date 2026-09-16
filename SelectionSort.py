a = [5, 3, 4, 1, 2]

for i in range(len(a)):
    min_index = i

    for j in range(i + 1, len(a)):
        if a[j] < a[min_index]:
            min_index = j

    a[i], a[min_index] = a[min_index], a[i]

print(a)
