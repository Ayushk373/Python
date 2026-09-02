

arr = [10, 20, 30, 40, 50]

print("Original Array:")
print(arr)


# 1. Traversal
print("\n1. Traversal:")
for element in arr:
    print(element)


# 2. Insertion
arr.append(60)
print("\n2. After Insertion:")
print(arr)


# 3. Insertion at a specific position
arr.insert(2, 25)
print("\nAfter inserting 25 at index 2:")
print(arr)


# 4. Deletion
arr.remove(30)
print("\n3. After Deletion of 30:")
print(arr)


# 5. Deletion using index
del arr[0]
print("\nAfter deleting element at index 0:")
print(arr)


# 6. Searching
search = 40

if search in arr:
    print("\n4. Searching:")
    print(search, "is found in the array")
else:
    print(search, "is not found in the array")


# 7. Updating
arr[1] = 100
print("\n5. After Updating:")
print(arr)


# 8. Display
print("\n6. Final Array:")
for i in range(len(arr)):
    print("Index", i, "=", arr[i])