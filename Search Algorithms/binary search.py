def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

# Example 1
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x1 = 4
print("Example 1 - Element found at index:", binary_search(arr1, x1))

# Example 2
arr2 = [10, 22, 35, 40, 55, 58, 60, 67]
x2 = 55
print("Example 2 - Element found at index:", binary_search(arr2, x2))

# Example 3
arr3 = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
x3 = 23
print("Example 3 - Element found at index:", binary_search(arr3, x3))
