"""
Insertion Sort

Idea:
The array is split into two.
The left part is the sorted area and the first element of the right part is the key.
Each iteration the key is inserted in the sorted area correctly and all elements larger than the key are shifted one position to the right.

Time: 
O(n^2) worst case and average case
O(n) best case (already sorted)
Space: O(n) for the copy
Stable: Yes

"""


def insertion_sort(arr: list) -> list:
    result = arr.copy()
    n = len(result)

    for i in range(1, n):
        key = result[i]
        j = i - 1
        while (j >= 0) and (result[j] > key):
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key

    return result
