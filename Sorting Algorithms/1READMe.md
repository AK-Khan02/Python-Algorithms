# Sorting Algorithms

## About
This folder is a curated collection of sorting algorithms implemented in Python. Sorting is a fundamental operation in computer science, essential in data processing and efficient algorithm design. This collection serves as an educational resource for understanding different sorting techniques and their characteristics.

## Algorithms Included

### Bubble Sort
- **File**: `Bubble Sort.py`
- **Description**: Bubble Sort is a simple comparison-based algorithm in which each pair of adjacent elements is compared and the elements are swapped if they are not in order. This process is repeated until no swaps are needed, indicating the list is sorted.

### Bucket Sort
- **File**: `Bucket Sort.py`
- **Description**: Bucket Sort distributes elements into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm or by recursively applying the bucket sort.

### Comb Sort
- **File**: `Comb Sort.py`
- **Description**: Comb Sort improves on Bubble Sort by eliminating turtles, or small values near the end of the list, since it uses a larger gap. As the gap decreases to 1, the algorithm becomes a bubble sort.

### Counting Sort
- **File**: `Counting Sort.py`
- **Description**: Counting Sort is an integer sorting algorithm that operates by counting the number of objects that possess distinct key values. It is efficient for sorting a small range of integers.

### Cycle Sort
- **File**: `Cycle Sort.py`
- **Description**: Cycle Sort is an in-place and unstable sorting algorithm theoretically optimal in terms of the total number of writes to the original array, making it useful for write-heavy memory scenarios.

### Heap Sort
- **File**: `Heap Sort.py`
- **Description**: Heap Sort is a comparison-based sorting technique based on a Binary Heap data structure. It is similar to selection sort where we first find the maximum element and place it at the end.

### Insertion Sort
- **File**: `Insertion Sort.py`
- **Description**: Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort.

### Merge Sort
- **File**: `Merge Sort.py`
- **Description**: Merge Sort is an efficient, stable, comparison-based, divide and conquer sorting algorithm. Most implementations produce a stable sort, meaning that the implementation preserves the input order of equal elements in the sorted output.

### Pigeonhole Sort
- **File**: `Pigeonhole Sort.py`
- **Description**: Pigeonhole Sorting is a sorting algorithm that is suitable for sorting lists of elements where the number of elements and the number of possible key values are approximately the same.

### Quick Sort
- **File**: `Quick Sort.py`
- **Description**: Quick Sort is an efficient sorting algorithm, serving as a systematic method for placing the elements of an array in order. It works by partitioning an array into two parts, then sorting the parts independently.

### Radix Sort
- **File**: `Radix Sort.py`
- **Description**: Radix Sort is a non-comparative integer sorting algorithm that sorts data with integer keys by grouping keys by the individual digits which share the same significant position and value.

### Selection Sort
- **File**: `Selection Sort.py`
- **Description**: Selection Sort is a simple comparison-based algorithm in which the list is divided into two parts, the sorted part at the left end and the unsorted part at the right end. Initially, the sorted part is empty and the unsorted part is the entire list.

### Shell Sort
- **File**: `Shell Sort.py`
- **Description**: Shell Sort is an in-place comparison sort. It can be seen as either a generalization of sorting by exchange (bubble sort) or sorting by insertion (insertion sort).
