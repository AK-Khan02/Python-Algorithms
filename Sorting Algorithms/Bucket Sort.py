def insertion_sort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up    
    return b    

def bucket_sort(arr):
    bucket = []
    slot_num = 10
    for i in range(slot_num):
        bucket.append([])
    
    for j in arr:
        index_b = int(slot_num * j)
        bucket[index_b].append(j)
    
    for i in range(slot_num):
        bucket[i] = insertion_sort(bucket[i])
        
    k = 0
    for i in range(slot_num):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
    return arr

# Example usage
examples = [
    [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434],
    [0.42, 0.32, 0.23, 0.52, 0.25],
    [0.9, 0.8, 0.7, 0.6, 0.5],
    [0.01, 0.02, 0.03, 0.04, 0.05],
    [0.5, 0.2, 0.9, 0.1, 0.1, 0.4]
]
for example in examples:
    bucket_sort(example)
    print(f"Sorted array: {example}")
