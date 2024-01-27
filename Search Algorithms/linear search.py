def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Example 1
arr1 = [3, 4, 1, 7, 9, 2]
x1 = 7
print("Example 1 - Element found at index:", linear_search(arr1, x1))

# Example 2
arr2 = [10, 23, 45, 53, 2]
x2 = 45
print("Example 2 - Element found at index:", linear_search(arr2, x2))

# Example 3
arr3 = [15, 5, 20, 35, 2, 42]
x3 = 3
print("Example 3 - Element not found, result:", linear_search(arr3, x3))
