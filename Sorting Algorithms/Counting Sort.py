def counting_sort(arr):
    max_val = max(arr)
    m = max_val + 1
    count = [0] * m
                
    for a in arr:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            arr[i] = a
            i += 1
    return arr

# Example usage
examples = [
    [1, 4, 1, 2, 7, 5, 2],
    [4, 2, 2, 8, 3, 3, 1],
    [1, 4, 1, 2, 7, 5, 2],
    [20, 18, 12, 8, 5, -2],
    [5, 3, 0, 2, 4, 1, 0, 5, 2]
]
for example in examples:
    counting_sort(example)
    print(f"Sorted array: {example}")
