from random import randint


def partition3(array: list[int], left: int, right: int) -> tuple[int, int]:
    """
    Partitions the array into three regions: < pivot, == pivot, and > pivot.
    This is a variation of the Dutch National Flag algorithm.

    Args:
        array (list[int]): The list to partition.
        left (int): The starting index of the segment to partition.
        right (int): The ending index of the segment to partition.

    Returns:
        tuple[int, int]: Indices m1 and m2 such that all elements between them are equal to the pivot.
    """
    # keep track of comparing element (pivot)
    x: int = array[left]

    # j and k are indices of comparison regions
    j: int = left + 1
    k: int = left + 1

    # move elements <= pivot to the left side
    for i in range(left + 1, right + 1):
        if array[i] <= x:
            array[j], array[i] = array[i], array[j]
            j += 1

    # create region where elements == pivot
    for i in range(left + 1, j):
        if array[i] == x:
            array[k], array[i] = array[i], array[k]
            k += 1

    # account for if swap zones overlap
    match_region_start: int = left
    match_region_end: int = min(j - (k - left), k)
    swap_region_start: int = max(j - (k - left), k)
    swap_region_end: int = j

    # move pivot-equal elements into correct position
    temp: list[int] = array[swap_region_start:swap_region_end]
    array[swap_region_start:swap_region_end] = array[match_region_start:match_region_end]
    array[match_region_start:match_region_end] = temp

    # indices where A[m1..m2] == pivot
    m1: int = left + (swap_region_end - k)
    m2: int = swap_region_end - 1

    return m1, m2


def randomized_quick_sort(array: list[int], left: int, right: int) -> None:
    """
    Sorts a list of integers in-place using 3-way randomized quicksort.

    Args:
        array (list[int]): The list of integers to sort.
        left (int): The starting index of the segment to sort.
        right (int): The ending index of the segment to sort.

    Returns:
        None
    """
    if left >= right:
        return

    # randomly choose pivot and swap with left
    k: int = randint(left, right)
    array[left], array[k] = array[k], array[left]

    # partition into three parts: < pivot, == pivot, > pivot
    m1, m2 = partition3(array, left, right)

    # recursively sort left and right segments
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    input_n = len(elements)
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
