import pytest
from sorting.bubble_sort import bubble_sort

def test_bubble_sort():
    test_cases = [
        [],
        [1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3, 1, 2, 3, 1],
        [-3, 0, -1, 2],
        ["b", "a", "c"]
    ]
    for data in test_cases:
        assert bubble_sort(data) == sorted(data)


def test_does_not_modify_input():
    data = [3, 1, 2]
    bubble_sort(data)
    assert data == [3, 1, 2]