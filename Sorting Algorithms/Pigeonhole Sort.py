def pigeonhole_sort(arr):
    min_val = min(arr)
    max_val = max(arr)
    size = max_val - min_val + 1

    holes = [0] * size

    for x in arr:
        assert type(x) is int, "integers only please"
        holes[x - min_val] += 1

    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            arr[i] = count + min_val
            i += 1

# Example usage
examples = [
    [8, 3, 2, 7, 4, 6, 8],
    [22, 11, 18, 15, 11, 12],
    [3, 6, 8, 10, 1, 2, 1],
    [5, 4, 3, 2, 1, 0],
    [1, 2, 3, 4, 5, 6]
]

for example in examples:
    pigeonhole_sort(example)
    print(f"Sorted array: {example}")
