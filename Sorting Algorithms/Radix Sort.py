def counting_sort_for_radix(input_list, significant_digit):
    bucket = [0] * 10
    output_list = [0] * len(input_list)

    for i in input_list:
        index = i // significant_digit
        bucket[index % 10] += 1

    for i in range(1, 10):
        bucket[i] += bucket[i - 1]

    i = len(input_list) - 1
    while i >= 0:
        index = input_list[i] // significant_digit
        output_list[bucket[index % 10] - 1] = input_list[i]
        bucket[index % 10] -= 1
        i -= 1

    for i in range(len(input_list)):
        input_list[i] = output_list[i]

def radix_sort(arr):
    max_val = max(arr)
    significant_digit = 1
    while max_val // significant_digit > 0:
        counting_sort_for_radix(arr, significant_digit)
        significant_digit *= 10

# Example usage
examples = [
    [170, 45, 75, 90, 802, 24, 2, 66],
    [121, 432, 564, 23, 1, 45, 788],
    [10, 100, 1000, 10000, 100000],
    [5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5]
]
for example in examples:
    radix_sort(example)
    print(f"Sorted array: {example}")
