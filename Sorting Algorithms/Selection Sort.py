def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Example usage
examples = [
    [64, 25, 12, 22, 11],
    [5, 1, 4, 2, 8],
    [0, 2, 34, 22, 10],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1]
]
for example in examples:
    selection_sort(example)
    print(f"Sorted array: {example}")
