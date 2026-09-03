arr = [10, 20, 30, 40, 50]

key = int(input("Enter element to search: "))

found = False

for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at index", i)
        found = True
        break

if found == False:
    print("Element not found")