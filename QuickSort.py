def quick_sort(a):
    if len(a) <= 1:
        return a

    pivot = a[0]

    left = []
    right = []

    for x in a[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return quick_sort(left) + [pivot] + quick_sort(right)


a = [5, 3, 8, 4, 2, 7, 1, 6]
print(quick_sort(a))
