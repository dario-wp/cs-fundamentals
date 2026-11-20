"""
Selection Sort

Idea:
The array is divided into a sorted and unsorted area.
Compare the start element of the iteration and swap with the smallest element.
After each iteration the starting position is incremented.

Time: O(n^2) in alle cases
Space O(n)
Stable: No
"""


def selection_sort(arr: list) -> list:
    result = arr.copy()
    n = len(result)
    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if result[min_index] > result[j]:
                min_index = j
        result[i], result[min_index] = result[min_index], result[i]

    return result
