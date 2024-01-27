def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

# Example usage
examples = [
    [23, 29, 15, 19, 31, 7, 9, 5, 2],
    [9, 8, 3, 7, 5, 6, 4, 1],
    [12, 34, 54, 2, 3],
    [1, 2, 3, 4, 5],
    [5, 3, 1, 2, 4]
]
for example in examples:
    shell_sort(example)
    print(f"Sorted array: {example}")
