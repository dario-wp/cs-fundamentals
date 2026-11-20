"""
Bubble Sort

Idea: Repeatedly compare adjacent elements and swap them if they are not in the correct order.
After each iteration the largest element is at the end of the array.
If after one iteration nothing was changed (swapped = False) then end the loop because the list is already sorted.

Worst Case: O(n^2)
Best Case: O(n)
Space: O(n)
Stable: Yes

"""


def bubble_sort(arr: list) -> list:
    result = arr.copy()
    n = len(result)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break

    return result
