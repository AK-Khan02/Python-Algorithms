def comb_sort(arr):
    def getNextGap(gap):
        gap = (gap * 10) // 13
        if gap < 1:
            return 1
        return gap

    n = len(arr)
    gap = n
    swapped = True

    while gap != 1 or swapped:
        gap = getNextGap(gap)
        swapped = False

        for i in range(0, n-gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True

# Example usage
examples = [
    [88, 55, 32, 12, 56, 82, 41, 8],
    [6, 4, 2, 9, 3, 8, 5, 1],
    [7, 3, 5, 8, 2, 6, 4, 1],
    [10, 22, 11, 5, 4, 3],
    [1, 2, 3, 4, 5, 6]
]

for example in examples:
    comb_sort(example)
    print(f"Sorted array: {example}")
