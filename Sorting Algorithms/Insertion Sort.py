def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Example usage
examples = [
    [22, 27, 16, 2, 18, 6],
    [3, 8, 5, 4, 1, 9],
    [-2, 45, 0, 11, -9],
    [1, 2, 3, 4, 5],
    [9, 8, 7, 6, 5]
]
for example in examples:
    insertion_sort(example)
    print(f"Sorted array: {example}")
