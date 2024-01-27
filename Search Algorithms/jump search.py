import math

def jump_search(arr, x):
    n = len(arr)
    step = math.sqrt(n)
    prev = 0

    while arr[int(min(step, n)-1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    while arr[int(prev)] < x:
        prev += 1

        if prev == min(step, n):
            return -1

    if arr[int(prev)] == x:
        return int(prev)

    return -1

# Example 1
arr1 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
x1 = 55
print("Example 1 - Element found at index:", jump_search(arr1, x1))

# Example 2
arr2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
x2 = 70
print("Example 2 - Element found at index:", jump_search(arr2, x2))

# Example 3
arr3 = [5, 7, 9, 11, 15, 20, 24, 30, 36, 40]
x3 = 15
print("Example 3 - Element found at index:", jump_search(arr3, x3))
