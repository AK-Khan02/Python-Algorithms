def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Example usage
examples = [
    [10, 7, 8, 9, 1, 5],
    [64, 34, 25, 12, 22, 11, 90],
    [1, 2, 3, 4, 5],
    [5, 6, 7, 2, 1, 8, 9, 3, 4],
    [-1, -4, -5, -2, -3, -6]
]
for example in examples:
    sorted_array = quick_sort(example)
    print(f"Sorted array: {sorted_array}")
