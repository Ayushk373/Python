arr = [10, 20, 30, 40, 50, 60, 70]

key = int(input("Enter element to search: "))

low = 0
high = len(arr) - 1

found = False

while low <= high:

    mid = (low + high) // 2

    if arr[mid] == key:
        print("Element found at index", mid)
        found = True
        break

    elif key < arr[mid]:
        high = mid - 1

    else:
        low = mid + 1

if found == False:
    print("Element not found")