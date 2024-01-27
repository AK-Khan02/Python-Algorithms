def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high and x >= arr[low] and x <= arr[high]:
        if low == high:
            if arr[low] == x: return low
            return -1

        pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))

        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return -1

# Example 1
arr1 = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
x1 = 18
print("Example 1 - Element found at index:", interpolation_search(arr1, x1))

# Example 2
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x2 = 7
print("Example 2 - Element found at index:", interpolation_search(arr2, x2))

# Example 3
arr3 = [10, 17, 24, 29, 35, 42, 49, 56, 63, 70]
x3 = 42
print("Example 3 - Element found at index:", interpolation_search(arr3, x3))
