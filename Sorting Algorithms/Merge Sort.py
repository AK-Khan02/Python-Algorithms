def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Example usage
examples = [
    [38, 27, 43, 3, 9, 82, 10],
    [12, 11, 13, 5, 6, 7],
    [5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5],
    [-1, -2, -3, -4, -5]
]
for example in examples:
    merge_sort(example)
    print(f"Sorted array: {example}")
