def cycle_sort(arr):
    writes = 0

    for cycleStart in range(0, len(arr) - 1):
        item = arr[cycleStart]

        pos = cycleStart
        for i in range(cycleStart + 1, len(arr)):
            if arr[i] < item:
                pos += 1

        if pos == cycleStart:
            continue

        while item == arr[pos]:
            pos += 1
        arr[pos], item = item, arr[pos]
        writes += 1

        while pos != cycleStart:
            pos = cycleStart
            for i in range(cycleStart + 1, len(arr)):
                if arr[i] < item:
                    pos += 1

            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]
            writes += 1

    return writes

# Example usage
examples = [
    [1, 8, 3, 9, 10, 10, 2, 4 ],
    [10, 3, 5, 1, 2, 8, 7, 6],
    [5, 1, 4, 2, 8, 9, 3],
    [20, 40, 50, 10, 30, 20, 60],
    [1, 2, 3, 4, 5, 6]
]

for example in examples:
    cycle_sort(example)
    print(f"Sorted array: {example}")
