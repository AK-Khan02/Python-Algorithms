def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage
examples = [
    [64, 34, 25, 12, 22, 11, 90],
    [5, 1, 4, 2, 8],
    [20, 20, -10, -10, 0, 0],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1]
]
for example in examples:
    bubble_sort(example)
    print(f"Sorted array: {example}")
